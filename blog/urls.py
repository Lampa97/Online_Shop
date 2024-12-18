from django.urls import path

from .views import ArticleListView, ArticleCreateView, ArticleDetailView


urlpatterns = [
    path("articles_list/", ArticleListView.as_view(), name="articles_list"),
    path("article_create/", ArticleCreateView.as_view(), name="article_create"),
    path("article_detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]
