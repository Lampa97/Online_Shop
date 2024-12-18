from django.shortcuts import render

from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Article
from django.views.generic import ListView, CreateView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = "blog/articles_list.html"
    context_object_name = "articles"

    def get(self, request):
        all_articles = Article.objects.all()
        paginator = Paginator(all_articles, 4)  # Show 4 products per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {"articles": page_obj}
        return render(request, "blog/articles_list.html", context)


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_create.html"
    context_object_name = "article"
    fields = ["title", "content", "preview"]
    success_url = reverse_lazy("articles_list")


    def form_valid(self, form):
        form.instance.is_published = True
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.views_counter += 1
        article.save()
        context = {"article": article}
        return render(request, "blog/article_detail.html", context)