from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def redirect_to_job_offers(request):
    url = '/emp/jobs/'
    return HttpResponseRedirect(redirect_to=url)


def redirect_to_login_page(request):
    url = '/accounts/login/'
    return HttpResponseRedirect(redirect_to=url)


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/emp/employers/'
    template_name = 'register.html'

