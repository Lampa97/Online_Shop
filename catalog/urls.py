from django.urls import path

from . import views
from .views import ContactsView, HomeListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("home/", HomeListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="single_product"),
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
]
