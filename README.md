🚀 Artisana
The Infrastructure for Digital Artisan Commerce

Artisana is a scalable multi-vendor marketplace platform engineered with Django.
It empowers independent artisans to launch and operate fully managed digital shops while customers seamlessly discover and purchase handcrafted products.

Designed with production architecture in mind, Artisana enforces structured business logic, stock integrity, role isolation, and marketplace governance — making it more than just an e-commerce project.

🌍 Vision

To provide artisans with a scalable digital commerce infrastructure that eliminates technical barriers while maintaining marketplace trust and operational control.

🏗 Platform Architecture

Artisana is built on a three-tier role architecture:

🛡 Admin

Marketplace governance & system authority

🏪 Artisan

Vendor storefront & product management

🛒 Customer

Discovery, checkout & order lifecycle

Strict Role-Based Access Control (RBAC) ensures workflow isolation and security boundaries.

✨ Core Features
🏪 Vendor Infrastructure (Artisan Domain)
Shop Activation Gate

Artisans must complete their shop profile before listing products.
This enforces marketplace consistency and prevents incomplete vendor states.

Required:

Shop Name

Description

Image

Contact Number

Product Lifecycle (Full CRUD)

Product creation & editing

Stock tracking

Secure vendor scoping

Deletion & updates

Real-Time Operational Dashboard

Dynamic metrics computed directly from system data:

Total Orders

Revenue

Inventory Count

Total Products

Order Workflow Engine

View incoming orders

Transition to “Shipped”

Structured state updates

WhatsApp Native Communication Layer

Instead of costly messaging APIs, Artisana implements:

Pre-filled WhatsApp message generation

Direct artisan-to-client communication

Zero external API cost

Seamless UX

CSV Data Export

Vendors can export structured order data for:

Accounting

Reporting

External processing

🛒 Customer Experience Layer
Marketplace Discovery

Product browsing

Detailed product pages

Advanced Search Engine

Database-level query filtering supports:

Product name search

Partial matching

Category filtering

Artisan shop lookup

Structured Checkout Flow

Automatic stock decrement

Order creation integrity

Personal order tracking

Stock mutations are strictly controlled to maintain data consistency.

🛡 Marketplace Governance (Admin Layer)

The Admin role operates as a platform oversight system:

User management

Artisan verification

Shop moderation

Product oversight

System-wide order visibility

Data integrity enforcement

Ensuring platform trust and operational monitoring.

🧠 Engineered Business Logic

Artisana enforces controlled system states:

Product listing blocked until shop completion

Automatic inventory mutation on purchase

Revenue derived from valid order states

Permission-protected views

Role-based order visibility

The system emphasizes controlled transitions over permissive CRUD behavior.

🛠 Technology Stack

Backend:

Django

Frontend:

Bootstrap

Database:

SQLite (Development)

PostgreSQL-ready (Production Migration Planned)

Data Handling:

CSV Export

Communication Layer:

Custom WhatsApp URL integration

📈 Scalability Roadmap

Artisana is architected for production evolution.

Planned upgrades:

PostgreSQL migration

Query optimization (select_related, prefetch_related)

Indexing for search acceleration

Redis caching

Celery background processing

Pagination for large datasets

Gunicorn + Nginx deployment

Cloud hosting (Render / DigitalOcean)

The platform supports horizontal scaling with infrastructure upgrades.

🔐 Security & Configuration

Environment-based configuration (.env)

Role-based permission isolation

Controlled stock mutation

Business rule enforcement

Production-ready structure

⚡ Quick Start
git clone https://github.com/mohammedsirDev/Plateforme-de-Gestion-de-Boutique-Artisanale.git
cd Plateforme-de-Gestion-de-Boutique-Artisanale
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🎯 Positioning

Artisana is not just an academic Django project.
It represents a structured, scalable commerce infrastructure model suitable for:

Artisan cooperatives

Regional digital marketplaces

Niche craft ecosystems

Emerging economy e-commerce solutions

👨‍💻 Founder

MOHAMMED SIR
GitHub: https://github.com/mohammedsirDev
