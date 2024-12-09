from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact, Product


def contacts(request):
    all_contacts = Contact.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"""Спасибо, {name}!
        Мы получили ваше сообщение: ({message}).
        Мы перезвоним вам по телефону: {phone}"""
        )
    return render(request, "catalog/contacts.html", {"contacts": all_contacts})


def home(request):
    last_5_products = Product.objects.all().order_by("-created_at")[:5]
    print(last_5_products)
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, "catalog/home.html", context=context)


def single_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "catalog/single_product.html", {"product": product})