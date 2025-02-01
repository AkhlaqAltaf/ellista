from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class ProjectsView(TemplateView):
    template_name = "projects.html"


class ProductsView(TemplateView):
    template_name = "products.html"

class NewsView(TemplateView):
    template_name = "news.html"

class GallaryView(TemplateView):
    template_name = "gallary.html"