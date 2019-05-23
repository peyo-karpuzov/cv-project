from django.shortcuts import render
from django.views import generic
from .models import JobOffer, EmployerUser
from cv.models import MotivationLetter


def job_is_of_employer(current_user, current_object):
    emp_user = EmployerUser.objects.all().filter(user__pk=current_user.id)[0]
    if current_object.user == emp_user or current_user.is_superuser:
        return True
    return False


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


class JobOffersList(generic.ListView):
    model = JobOffer
    template_name = 'job_offers_list.html'
    context_object_name = 'jobs'


class JobOfferDetails(generic.DetailView):
    model = JobOffer
    template_name = 'job_offer_details.html'
    context_object_name = 'emp'

    def get_context_data(self, **kwargs):
        context = super(JobOfferDetails, self).get_context_data(**kwargs)
        context['letter'] = MotivationLetter.objects.all().filter(job_offer=self.get_object())
        return context


