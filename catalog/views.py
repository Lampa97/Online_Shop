from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"""Спасибо, {name}! 
        Мы получили ваше сообщение: ({message}).
        Мы перезвоним вам по телефону: {phone}""")
    return render(request, 'catalog/contacts.html')


def home(request):
    last_5_products = Product.objects.all().order_by('-created_at')[:5]
    print(last_5_products)
    return render(request, 'catalog/home.html')
