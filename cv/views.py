from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from emp.models import EmployerUser

from .models import MotivationLetter
from . import forms


class MotivationLetterDetails(generic.DetailView):
    model = MotivationLetter
    template_name = 'motivation_letter_details.html'
    context_object_name = 'letter'


class ApplicantCreate(generic.CreateView):
    form_class = forms.ApplicantUserForm
    template_name = 'applicant_create.html'
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        user_id = EmployerUser.objects.all().filter(user__pk=self.request.user.id)
        if not user_id:
            form.instance.user = self.request.user
            return super().form_valid(form)
        return HttpResponse("The user is already an Employer. Users can be only applicants or employers.")