from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact, Product, Category


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


def add_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_name = request.POST.get("category")
        image = request.FILES.get("image")

        category = Category.objects.get(name=category_name)

        print(image)

        Product.objects.create(
            name=name, description=description, price=price, category_id=category.pk, image=image
        )

        return HttpResponse("Продукт успешно добавлен")


    return render(request, "catalog/add_product.html", {"categories": categories})