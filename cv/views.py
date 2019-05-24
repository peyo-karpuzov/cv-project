from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from emp.models import EmployerUser

from .models import MotivationLetter, ApplicantUser, CVGeneral, CVWorkPlaces, CVEducation, CVLanguages
from . import forms


def redirect_to_user_profile(request):
    url_redirect = f'/cv/home/{request.user.id}/'
    return HttpResponseRedirect(redirect_to=url_redirect)


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


class ApplicantProfile(generic.DetailView):
    model = ApplicantUser
    template_name = 'applicant_home.html'
    context_object_name = 'applicant'


class CVGeneralCreate(generic.CreateView):
    template_name = 'cv_general_create.html'
    form_class = forms.CVGeneralForm
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        form.instance.applicant_user = ApplicantUser.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)


class CVWorkplaceCreate(generic.CreateView):
    template_name = 'cv_workplace_create.html'
    form_class = forms.CVWorkplaceForm
    success_url = '/emp/jobs/'


class CVEducationCreate(generic.CreateView):
    template_name = 'cv_education_create.html'
    form_class = forms.CVEducationForm
    success_url = '/emp/jobs/'


class CVLanguagesCreate(generic.CreateView):
    template_name = 'cv_languages_create.html'
    form_class = forms.CVLanguagesForm
    success_url = '/emp/jobs/'


class CVList(generic.ListView):
    model = CVGeneral
    template_name = 'cv_list.html'
    context_object_name = 'cv'


class CVDetails(generic.DetailView):
    model = CVGeneral
    template_name = 'cv_details.html'
    context_object_name = 'general'

    def get_context_data(self, **kwargs):
        context = super(CVDetails, self).get_context_data(**kwargs)
        context['workplace'] = CVWorkPlaces.objects.filter(cv_general=self.get_object()).order_by('-start_date')
        context['education'] = CVEducation.objects.filter(cv_general=self.get_object()).order_by('-start_date')
        context['languages'] = CVLanguages.objects.filter(cv_general=self.get_object())
        return context


class CVEdit(generic.UpdateView):
    model = CVGeneral
    template_name = 'cv_general_create.html'
    form_class = forms.CVGeneralForm
    success_url = '/emp/jobs/'


class CVDelete(generic.DeleteView):
    model = CVGeneral
    template_name = 'cv_delete.html'
    context_object_name = 'cv'
    success_url = '/emp/jobs/'