from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def redirect_to_common_profile(request):
    url = f'/accounts/profile/common/{request.user.id}'
    return HttpResponseRedirect(redirect_to=url)


# def redirect_to_applicant_create(request):
#     a = request.user.id
#     url = f'/cv/applicant/create/'
#     return HttpResponseRedirect(redirect_to=url)


def redirect_to_login_page(request):
    url = '/accounts/login/'
    return HttpResponseRedirect(redirect_to=url)


class CommonProfile(generic.DetailView):
    model = User
    template_name = 'unregistered_common_profile.html'
    context_object_name = 'user'


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'register.html'

