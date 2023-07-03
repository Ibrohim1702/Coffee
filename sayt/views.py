from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )

        ctx = {
            "contact": contact,
        }
    return render(requests, "index.html", ctx)

def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)

def contact(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )

        ctx = {
            "contact": contact,
        }
    return render(requests, "contact.html", ctx)

def gallery(requests):
    ctx = {

    }
    return render(requests, "gallery.html", ctx)

def services(requests):
    ctx = {

    }
    return render(requests, "services.html", ctx)