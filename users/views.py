from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
