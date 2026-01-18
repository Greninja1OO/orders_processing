from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#TODOS: class didn't work try to find another way
#!simple danger implement jwt authorization in future
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_no = forms.CharField(required=True, max_length=15)
    class meta:
        model=User
        fields=["username","email","mobile_no","password1","password2"]

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login:login")
    else:
        form = RegistrationForm()

    return render(request, "register/register.html", {"form": form})
