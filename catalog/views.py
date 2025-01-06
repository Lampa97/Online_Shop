from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import ProductForm
from .models import Category, Contact, Product

ALL_CATEGORIES = Category.objects.all()


class ContactsView(TemplateView):
    model = Contact
    template_name = "catalog/contacts.html"

    def get(self, request):
        all_contacts = Contact.objects.all()
        context = {"categories": ALL_CATEGORIES, "contacts": all_contacts}

        return render(request, "catalog/contacts.html", context)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"""Спасибо, {name}!
                Мы получили ваше сообщение: ({message}).
                Мы перезвоним вам по телефону: {phone}"""
        )


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get(self, request):
        all_products = Product.objects.all()
        paginator = Paginator(all_products, 4)  # Show 4 products per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {"products": page_obj, "categories": ALL_CATEGORIES}
        return render(request, "catalog/home.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/single_product.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("home")


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = "product"
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("home")
