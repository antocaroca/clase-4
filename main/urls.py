from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about-us/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    
]