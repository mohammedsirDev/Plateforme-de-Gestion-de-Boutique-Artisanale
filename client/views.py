# Authentication utilities
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Models imports
from product import models as products_models
from artisan import models as artisan_models
from category import models as category_models
from client import models as client_modeles
from client import forms as client_form
from order import models as order_models
from product import models as product_models

# Django ORM utilities
from django.db.models import Count, Q
from django.db import transaction

# Messaging framework
from django.contrib import messages

# Django shortcuts
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    """
    Homepage view.

    Displays:
    - Latest products
    - Top artisans (based on product count)
    - Available categories
    """

    products = products_models.Products.objects.all()

    categories = category_models.Category.objects.all()

    # Annotate artisans with product count for ranking display
    artisans = artisan_models.Artisan.objects.annotate(
        product_count=Count('products_artisan')
    )[:4]

    context = {
        "products": products,
        "artisans": artisans,
        "categories": categories
    }

    return render(request, "client/index.html", context)


def product_detail(request, id):
    """
    Product detail page.

    Displays full product information.
    """

    product = products_models.Products.objects.get(id=id)

    return render(
        request,
        "client/product_detail.html",
        {"product": product}
    )


def search(request):
    """
    Product search system.

    Supports:
    - Name search
    - Artisan shop name search
    - Category filtering
    """

    query = request.GET.get("q")
    category_id = request.GET.get('category')

    products = products_models.Products.objects.all()

    # Category filter
    if category_id:
        products = products.filter(category_id=category_id)

    categories = category_models.Category.objects.all()


    # Text search (case-insensitive)
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(artisan__shop_name__icontains=query)
        )

    return render(
        request,
        "client/search_results.html",
        {
            "products": products,
            "query": query,
            "categories": categories
        }
    )


@login_required
def checkout(request, id):
    """
    Checkout system.

    Business rules:
    - Only authenticated client users can checkout.
    - Prevent checkout if product stock is zero.
    - Ensure atomic transaction when creating orders.
    """

    product = get_object_or_404(product_models.Products, id=id)

    # Verify client profile existence
    if not client_modeles.Clinet.objects.filter(user=request.user).exists():
        messages.error(request, "Veuillez vous connecter avec un compte client.")
        logout(request)
        return redirect("userauths:login_view")

    if request.method == "POST":
        form = client_form.AddOrder(request.POST)

        if form.is_valid():

            # Stock protection rule
            if product.stock <= 0:
                messages.error(request, "Produit en rupture de stock.")

                return render(
                    request,
                    "client/checkout.html",
                    {
                        "form": form,
                        "product": product,
                        "price": product.price
                    }
                )

            # Atomic transaction ensures data consistency
            with transaction.atomic():
                order = form.save(commit=False)
                order.artisan = product.artisan
                order.client = request.user.client
                order.total_amount = product.price
                order.save()

                # Decrease stock after successful order
                product.stock -= 1
                product.save()

            messages.success(request, "Commande confirmée avec succès.")
            return redirect("client:commande_confirm")

    else:
        form = client_form.AddOrder()

    return render(
        request,
        "client/checkout.html",
        {
            "form": form,
            "product": product,
            "price": product.price
        }
    )


@login_required
def commande_confirm(request):
    """
    Order confirmation page.
    """
    return render(request, "client/commande_confirm.html")


@login_required
def Page_des_commandes_clients(request):
    """
    Display client order history.
    """

    if not hasattr(request.user, "client"):
        messages.error(request, "Veuillez vous connecter avec un compte client.")
        return redirect("userauths:login_view")

    client = request.user.client

    # Retrieve client orders sorted by latest
    orders = order_models.Order.objects.filter(
        client=client
    ).order_by("-created_at")

    return render(
        request,
        "client/Page_des_commandes_clients.html",
        {"orders": orders}
    )