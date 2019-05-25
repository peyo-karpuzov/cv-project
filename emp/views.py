from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from cv.models import MotivationLetter, ApplicantUser
from cv.forms import MotivationLetterForm

from .models import JobOffer, EmployerUser
from .forms import EmployerUserForm, JobOfferForm


def have_access_to_modify(current_user, current_object):
    if ApplicantUser.objects.all().filter(user=current_user):
        return True
    elif current_user.is_superuser:
        return True
    elif current_object.employer_user == EmployerUser.objects.all().filter(user=current_user):
        return True
    else:
        return False


class EmployerCreate(generic.CreateView):
    form_class = EmployerUserForm
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
    form_class = EmployerUserForm
    success_url = '/emp/employers/'


class EmployerDelete(generic.DeleteView):
    model = EmployerUser
    template_name = 'employer_delete.html'
    context_object_name = 'employer'
    success_url = '/emp/employers/'


class JobOfferCreate(generic.CreateView):
    form_class = JobOfferForm
    template_name = 'job_offer_create.html'
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        user_id = ApplicantUser.objects.all().filter(user__pk=self.request.user.id)
        if not user_id:
            form.instance.employer_user = EmployerUser.objects.filter(user=self.request.user)[0]
            return super().form_valid(form)
        return HttpResponse("The user must be an employer.")


class JobOffersList(generic.ListView):
    model = JobOffer
    template_name = 'job_offers_list.html'
    context_object_name = 'jobs'


class JobOffersUserList(generic.ListView):
    model = JobOffer
    template_name = 'job_offers_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        profile_user = EmployerUser.objects.all().filter(user__pk=self.request.user.id)[0]
        jobs = JobOffer.objects.filter(employer_user=profile_user)
        if jobs:
            return jobs
        else:
            return []


class JobOfferDetails(LoginRequiredMixin, generic.DetailView):
    model = JobOffer
    #login_url = '/accounts/login/'
    template_name = 'job_offer_details.html'
    context_object_name = 'job'

#     def get_context_data(self, **kwargs):
#         context = super(JobOfferDetails, self).get_context_data(**kwargs)
#         context['letter'] = MotivationLetter.objects.all().filter(job_offer=self.get_object())
#         context['form'] = MotivationLetterForm
#         if have_access_to_modify(current_user=self.request.user, current_object=self.get_object()):
#             context['can_modify'] = True
#         else:
#             context['can_modify'] = False
#         return context
#
#     def post(self, request, pk):
#         url = f'/emp/jobs/{self.get_object().id}/'
#         post_values = request.POST.copy()
#         form = MotivationLetterForm(post_values)
#
#         if form.is_valid():
#             applicant_user = ApplicantUser.objects.all().filter(user__pk=request.user.id)[0]
#             post_values['job_offer'] = self.get_object()
#             motivation_letter = MotivationLetter(
#                 cv_general=post_values['cv_general'],
#                 text=post_values['text'],
#                 job_offer=self.get_object(),
#                 applicant_user=applicant_user
#             )
#             motivation_letter.save()
#             return HttpResponseRedirect(url)
#         else:
#             raise(Exception(form.errors))


class JobOfferEdit(generic.UpdateView):
    model = JobOffer
    template_name = 'job_offer_create.html'
    form_class = JobOfferForm
    success_url = '/emp/jobs/'


class JobOfferDelete(generic.DeleteView):
    model = JobOffer
    template_name = 'job_offer_delete.html'
    context_object_name = 'job'
    success_url = '/emp/jobs/'