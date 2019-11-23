from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from main import forms
from main import models
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

class SignupView(FormView):
    template_name = "signup.html"
    form_class = forms.UserCreationForm
    
    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)

        form.send.mail()
        messages.info(self.request, "Te has logueado correctamente")
        return response


def home(request):
    """
    Página de inicio

    """
    return (render(request, "home.html", {}))

class ContactUsView(FormView):
    """
    Formulario de contacto
    
    """
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

class ProductList(ListView):
    """
    Lista de productos
    
    """

    template_name = "product_list.html"

    def get_queryset(self):
        products = models.Producto.objects.all()
        return products.order_by("name")
