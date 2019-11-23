from django.urls import path
from django.views.generic import TemplateView, FormView
from main import views

urlpatterns = [
    path('about-us/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('contact-us', views.ContactUsView.as_view(), name="contact-us",),
    path('products', views.ProductList.as_view(), name="products",),
    path('signup', views.SignupView.as_view(), name="signup",),
]