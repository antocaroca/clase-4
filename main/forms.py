from django import forms
from django.core.mail import send_mail
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationform)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        message = "From:{0}\n{1}".format(
            self.cleaned_data["name"],
            self.cleaned_data["message"],
        )

        send_mail(
            "Site message",
            message,
            "site@mybooktime.cl",
            ["customer@mybooktime.cl"],
            fail_silently=False
        )

class UserCreationForm(DjangoUserCreationform):
    """
    Formulario de creación de usuario
    """
    class meta(DjangoUserCreationform.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email":UsernameField}

    def send_mail(self):
        message = "Welcome {}".format(self.cleaned_data["email"])
        send_mail(
            "Welcome to BookTime",
            message,
            "site@mybooktime.cl",
            [self.cleaned_data["email"]],
            fail_silently=True
        )
