from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class ProjectsView(TemplateView):
    template_name = "projects.html"