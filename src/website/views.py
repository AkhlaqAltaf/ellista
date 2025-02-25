from src.website.models import Project, GalleryMedia
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string

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

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Prepare the email
        subject = f"New message from {name}"
        body = render_to_string('mail.html', {
            'name': name,
            'email': email,
            'message': message,
        })
        recipient_list = ['ellista-@hotmail.com']
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
            html_message=body
        )

        return HttpResponseRedirect(reverse('website:contact'))
class DownloadView(TemplateView):
    template_name = "download.html"