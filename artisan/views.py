from django.shortcuts import render, redirect
from product import forms as forms_product
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from artisan.models import Artisan
from product.models import Products
from artisan import forms as fomrs_artisan
from order import models as modeles_orders
# URL encoding for WhatsApp message generation
from urllib.parse import quote

# Database aggregation utilities
from django.db.models import Sum


@login_required
def dashboard_artisan(request):
    """
    Artisan dashboard view.
    Displays key marketplace metrics including:
    - Total orders
    - Revenue
    - Total stock
    - Total products
    """

    # Get artisan profile associated with logged-in user
    artisan = Artisan.objects.filter(user=request.user).first()

    # If user is not an artisan, redirect to homepage
    if not artisan:
        return redirect("home")

    # Count total orders for artisan
    total_orders = artisan.artisan_order.count()

    # Calculate total revenue using aggregation
    revenue = artisan.artisan_order.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    # Calculate total stock across all artisan products
    total_stock = artisan.products_artisan.aggregate(
        total=Sum("stock")
    )["total"] or 0

    # Count total products owned by artisan
    total_products = artisan.products_artisan.count()

    context = {
        "artisan": artisan,
        "total_orders": total_orders,
        "revenue": revenue,
        "total_stock": total_stock,
        "total_products": total_products,
    }

    return render(request, "artisan/dashboard_artisan.html", context)


@login_required
def add_product(request):
    """
    Allow artisan to add new products.

    Security rule:
    - Product creation is allowed only if artisan profile is completed.
    """

    artisan = Artisan.objects.filter(user=request.user).first()

    if not artisan:
        return redirect("home")

    # Ensure artisan profile is fully completed before product creation
    if not all([
        artisan.shop_name,
        artisan.shop_description,
        artisan.shop_image,
        artisan.phone
    ]):
        messages.warning(
            request,
            "Veuillez compléter le profil de votre boutique avant d'ajouter un produit."
        )
        return redirect("artisan:setup_artisan")

    # Retrieve artisan products
    products = Products.objects.filter(artisan=artisan)

    if request.method == "POST":
        form = forms_product.ProductFormAdd(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.artisan = artisan
            product.save()
            return redirect("artisan:add_product")

    else:
        form = forms_product.ProductFormAdd()

    return render(request, "artisan/add_product.html", {
        "form": form,
        "products": products
    })


@login_required
def delete_product(request, id):
    """
    Delete product owned by authenticated artisan.
    """

    product = get_object_or_404(
        Products,
        id=id,
        artisan__user=request.user
    )

    product.delete()
    return redirect("artisan:add_product")


@login_required
def edit_product(request, id):
    """
    Edit product information.

    Security rule:
    - Only product owner can edit product data.
    """

    product = get_object_or_404(
        Products,
        id=id,
        artisan__user=request.user
    )

    if request.method == "POST":
        form = forms_product.ProductFormAdd(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect("artisan:add_product")

    else:
        form = forms_product.ProductFormAdd(instance=product)

    return render(request, "artisan/edit_product.html", {"form": form})


@login_required
def setup_artisan(request):
    """
    Artisan profile setup view.

    Allows artisan to complete shop profile information.
    """

    artisan = Artisan.objects.filter(user=request.user).first()

    if not artisan:
        return redirect("home")

    if request.method == "POST":
        form = fomrs_artisan.ArtisanSetupForm(
            request.POST,
            request.FILES,
            instance=artisan
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_profile_completed = True
            profile.save()
            return redirect("artisan:add_product")

    else:
        form = fomrs_artisan.ArtisanSetupForm(instance=artisan)

    return render(request, "artisan/setup_artisan.html", {"form": form})


@login_required
def my_orders(request):
    """
    Display artisan orders with status statistics.
    """

    orders = modeles_orders.Order.objects.filter(
        artisan__user=request.user
    )

    pending_orders = modeles_orders.Order.objects.filter(
        artisan__user=request.user,
        status='PENDING'
    ).count()

    shipped_orders = modeles_orders.Order.objects.filter(
        artisan__user=request.user,
        status='SHIPPED'
    ).count()

    delivered_orders = modeles_orders.Order.objects.filter(
        artisan__user=request.user,
        status='DELIVERED'
    ).count()

    cancelled_orders = modeles_orders.Order.objects.filter(
        artisan__user=request.user,
        status='CANCELLED'
    ).count()

    context = {
        "pending_orders": pending_orders,
        "SHIPPED_orders": shipped_orders,
        "DELIVERED_orders": delivered_orders,
        "CANCELLED_orders": cancelled_orders,
        "orders": orders,
    }

    return render(request, 'artisan/orders.html', context)


@login_required
def update_order(request, pk):
    """
    Update order status.

    Business rule:
    - When order status changes to SHIPPED,
      a WhatsApp notification is generated automatically.
    """

    order = get_object_or_404(
        modeles_orders.Order,
        id=pk,
        artisan__user=request.user
    )

    old_status = order.status

    if request.method == 'POST':
        form = fomrs_artisan.OrderUpdateForm(request.POST, instance=order)

        if form.is_valid():
            order = form.save()

            # Trigger WhatsApp communication only when status changes to SHIPPED
            if order.status == "SHIPPED" and old_status != "SHIPPED":

                # Clean phone number format
                phone = order.phone.strip()
                phone = phone.replace("+", "").replace(" ", "")

                # Convert Moroccan number format (06xxxxxxx → 2126xxxxxxx)
                if phone.startswith("0"):
                    phone = "212" + phone[1:]

                # Compose WhatsApp message
                message = (
                    f"Bonjour {order.first_name},\n\n"
                    f"Votre commande #{order.id} a été expédiée 🚚✨\n\n"
                    "Merci pour votre confiance ❤️"
                )

                whatsapp_url = f"https://wa.me/{phone}?text={quote(message)}"

                return redirect(whatsapp_url)

            return redirect('artisan:orders')

    else:
        form = fomrs_artisan.OrderUpdateForm(instance=order)

    return render(request, 'artisan/update_order.html', {'form': form})


import csv
from django.http import HttpResponse

@login_required
def export_orders(request):
    """
    Export artisan orders as CSV file.

    Security rule:
    - Only authenticated artisan can export their own orders.
    """

    if not hasattr(request.user, "artisan"):
        return HttpResponse("Unauthorized", status=403)

    artisan = request.user.artisan

    orders = modeles_orders.Order.objects.filter(artisan=artisan)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response, delimiter=';')

    # CSV Header
    writer.writerow([
        "ID Commande",
        "Client",
        "Montant Total",
        "Statut",
        "Date",
        "Adresse",
        "Téléphone",
    ])

    # Write order data
    for order in orders:
        writer.writerow([
            order.id,
            order.client.user.email,
            order.total_amount,
            order.status,
            order.created_at.strftime("%Y-%m-%d %H:%M"),
            order.adresse,
            order.phone,
        ])

    return response