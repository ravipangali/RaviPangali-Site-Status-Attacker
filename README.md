RaviPangali Sites Status Attacker
A django package made by Ravi Pangali for down those sites which are made by himself
Installation
Install from GitHub using pip:
pip install git+https://github.com/ravipangali/RaviPangali-Site-Status-Attacker

Setup

Add django_sitestatus and rest_framework to INSTALLED_APPS in your Django settings:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_sitestatus',
]


Include the URLs in your project's urls.py:

from django.urls import include, path

urlpatterns = [
    ...
    path('', include('ravipangali_sites_status_attacker.urls')),
]


Add the middleware to MIDDLEWARE in your Django settings:

MIDDLEWARE = [
    ...
    'ravipangali_sites_status_attacker.middleware.SiteStatusMiddleware',
]


Run migrations to create the SiteStatus model:

python manage.py makemigrations
python manage.py migrate

Usage

Model: The SiteStatus model stores the site status (True for up, False for maintenance) and a description.
API Endpoint: Use the /change-site-status/ endpoint to update the site status via POST requests. Example:

curl -X POST -H "Content-Type: application/json" -d '{"status": true, "description": "Site is up"}' http://yourdomain.com/change-site-status/


Middleware: Automatically shows a maintenance page (site_status.html) when the site status is False or no status exists, except for admin, static, or media URLs.
Template: The site_status.html template displays the maintenance message and auto-refreshes every 30 seconds.

License
MIT License
