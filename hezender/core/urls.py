from django.urls import path

from .views import About, BlogDetailView, BlogListView, Contact, Events, Home, Services

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
    path('events/', Events.as_view(), name='events'),
    path('contact/', Contact.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
