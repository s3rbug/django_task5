from django.shortcuts import render
from django.http import HttpRequest
from .sources import SERVICES, PRODUCTS


def services_page(request: HttpRequest):
    return render(request, "services.html", {"services": SERVICES})


def software_page(request: HttpRequest):
    return render(request, "software.html", {"products": PRODUCTS})


def home_page(request: HttpRequest):
    return render(request, "home.html")


def contacts_page(request: HttpRequest):
    return render(request, "contacts.html", {"address": "м. Київ, вул. Тестова, 1",
                                             "email": "eshop@gmail.com",
                                             "facebook_url": "https://www.facebook.com/ssternenko",
                                             "telegram_url": "https://t.me/ssternenko"})
