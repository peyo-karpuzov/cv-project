from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from cv.models import MotivationLetter, ApplicantUser

from .models import JobOffer, EmployerUser
from . import forms


def job_is_of_employer(current_user, current_object):
    emp_user = EmployerUser.objects.all().filter(user__pk=current_user.id)[0]
    if current_object.user == emp_user or current_user.is_superuser:
        return True
    return False


class EmployerCreate(generic.CreateView):
    form_class = forms.EmployerUserForm
    template_name = 'employer_create.html'
    success_url = '/emp/employers/'

    def form_valid(self, form):
        user_id = ApplicantUser.objects.all().filter(user__pk=self.request.user.id)
        if not user_id:
            form.instance.user = self.request.user
            return super().form_valid(form)
        return HttpResponse("The user is already an Applicant. Users can be only applicants or employers.")


class EmployersList(generic.ListView):
    model = EmployerUser
    template_name = 'employers_list.html'
    context_object_name = 'emps'


class EmployerDetails(generic.DetailView):
    model = EmployerUser
    template_name = 'employer_details.html'
    context_object_name = 'emps'

    def get_context_data(self, **kwargs):
        context = super(EmployerDetails, self).get_context_data(**kwargs)
        context['jobs'] = JobOffer.objects.all().filter(employer_user=self.get_object())
        return context


class EmployerEdit(generic.UpdateView):
    model = EmployerUser
    template_name = 'employer_create.html'
    context_object_name = 'form'
    form_class = forms.EmployerUserForm
    success_url = '/emp/employers/'


class EmployerDelete(generic.DeleteView):
    model = EmployerUser
    template_name = 'employer_delete.html'
    context_object_name = 'employer'
    success_url = '/emp/employers/'


class JobOfferCreate(generic.CreateView):
    form_class = forms.JobOfferCreate
    template_name = 'job_offer_create.html'
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        form.instance.employer_user = EmployerUser.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)


class JobOffersList(generic.ListView):
    model = JobOffer
    template_name = 'job_offers_list.html'
    context_object_name = 'jobs'


class JobOfferDetails(generic.DetailView):
    model = JobOffer
    template_name = 'job_offer_details.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super(JobOfferDetails, self).get_context_data(**kwargs)
        context['letter'] = MotivationLetter.objects.all().filter(job_offer=self.get_object())
        return context


class JobOfferEdit(generic.UpdateView):
    model = JobOffer
    template_name = 'job_offer_create.html'
    form_class = forms.JobOfferCreate
    success_url = '/emp/jobs/'


class JobOfferDelete(generic.DeleteView):
    model = JobOffer
    template_name = 'job_offer_delete.html'
    context_object_name = 'job'
    success_url = '/emp/jobs/'