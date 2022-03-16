from typing import Any, Dict

from django.views.generic import DetailView, ListView, TemplateView

from .models import BlogModel, EventModel


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'core/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['blogs'] = BlogModel.objects.all()
        return context


class BlogListView(ListView):
    model = BlogModel
    template_name = 'core/blog_list.html'
    context_object_name = 'blogs'


class Events(TemplateView):
    template_name = 'core/events.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['events'] = EventModel.objects.all()
        return context


class Contact(TemplateView):
    template_name = 'public/contact.html'


class About(TemplateView):
    template_name = 'public/about.html'


class Home(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['blogs'] = BlogModel.objects.all()[0:2]
        context['events'] = EventModel.objects.all()[0:2]
        return context


class Services(TemplateView):
    template_name = 'core/services.html'
