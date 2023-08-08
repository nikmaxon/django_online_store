from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'

