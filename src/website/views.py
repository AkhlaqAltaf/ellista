from django.views.generic import TemplateView
from src.website.models import Project, GalleryMedia

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the first 3 projects
        context['projects'] = Project.objects.all()[:3]
        return context

class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all projects
        context['projects'] = Project.objects.all()
        return context

class GalleryView(TemplateView):
    template_name = "gallery.html"  # Corrected the template name from "gallery.html" to "gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all gallery media
        context['gallery_media'] = GalleryMedia.objects.all()
        return context

class ProductsView(TemplateView):
    template_name = "products.html"

class NewsView(TemplateView):
    template_name = "news.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class DownloadView(TemplateView):
    template_name = "download.html"