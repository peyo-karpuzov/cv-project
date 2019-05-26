from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# from emp.models import EmployerUser
from accounts.views import redirect_to_common_profile

from .models import MotivationLetter, ApplicantUser, CVGeneral, CVWorkPlaces, CVEducation, CVLanguages
from . import forms


# def redirect_to_user_profile(request):
#     url_redirect = f'/cv/home/{request.user.id}/'
#     return HttpResponseRedirect(redirect_to=url_redirect)


class ApplicantCreate(generic.CreateView):
    form_class = forms.ApplicantUserForm
    template_name = 'applicant_create.html'
    success_url = f'/emp/jobs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    # def form_valid(self, form):
    #     user_id = EmployerUser.objects.all().filter(user__pk=self.request.user.id)
    #     if not user_id:
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)
    #     return HttpResponse("The user is already an Employer. Users can be only applicants or employers.")


class ApplicantProfile(generic.DetailView):
    model = ApplicantUser
    template_name = 'applicant_home.html'
    context_object_name = 'applicant'

    # def get_queryset(self):
    #     return ApplicantUser.objects.all().filter(user__pk=self.request.user.id)[0]


class CVGeneralCreate(generic.CreateView):
    template_name = 'cv_general_create.html'
    form_class = forms.CVGeneralForm
    success_url = '/cv/workplace/create/'

    def form_valid(self, form):
        form.instance.applicant_user = ApplicantUser.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)


class CVWorkplaceCreate(generic.CreateView):
    template_name = 'cv_workplace_create.html'
    form_class = forms.CVWorkplaceForm
    success_url = '/cv/workplace/create/'


class CVEducationCreate(generic.CreateView):
    template_name = 'cv_education_create.html'
    form_class = forms.CVEducationForm
    success_url = '/cv/education/create/'


class CVLanguagesCreate(generic.CreateView):
    template_name = 'cv_languages_create.html'
    form_class = forms.CVLanguagesForm
    success_url = '/cv/language/create/'


class CVList(generic.ListView):
    model = CVGeneral
    template_name = 'cv_list.html'
    context_object_name = 'cv'


class CVUserList(generic.ListView):
    model = CVGeneral
    template_name = 'cv_list.html'
    context_object_name = 'cv'

    def get_queryset(self):
        profile_user = ApplicantUser.objects.all().filter(user__pk=self.request.user.id)[0]
        cv = CVGeneral.objects.filter(applicant_user=profile_user)
        if cv:
            return cv
        else:
            return []


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


class CVEdit(LoginRequiredMixin, generic.UpdateView):
    model = CVGeneral
    template_name = 'cv_general_create.html'
    form_class = forms.CVGeneralForm
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        form.instance.applicant_user = ApplicantUser.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)

    def get(self, request, pk):
        if self.request.user.id == self.get_object().applicant_user.user.id:
            a = CVGeneral.objects.get(pk=pk)
            form = forms.CVGeneralForm(request.POST or None, instance=a)
            return render(request, 'cv_general_create.html', {'form': form})
        else:
            return render(request, 'permission_denied.html')


class CVDelete(generic.DeleteView):
    model = CVGeneral
    login_url = '/accounts/login/'
    template_name = 'cv_delete.html'
    context_object_name = 'cv'
    success_url = '/emp/jobs/'

    def get(self, request, pk):
        if self.request.user.id == self.get_object().applicant_user.user.id:
            return render(request, 'cv_delete.html', {'cv': self.get_object()})
        return render(request, 'permission_denied.html')

    def post(self, request, pk):
        if self.request.user.id == self.get_object().applicant_user.user.id:
            cv = self.get_object()
            cv.delete()
            return HttpResponseRedirect('/emp/jobs/')


class SendLetterCreate(generic.CreateView):
    template_name = 'motivation_letter_create.html'
    form_class = forms.MotivationLetterForm
    success_url = '/emp/jobs/'

    def form_valid(self, form):
        user = ApplicantUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.applicant_user = user
        return super().form_valid(form)

    # def form_valid(self, form):
    #     user_id = EmployerUser.objects.all().filter(user__pk=self.request.user.id)
    #     if not user_id:
    #         user = ApplicantUser.objects.all().filter(user__pk=self.request.user.id)[0]
    #         form.instance.applicant_user = user
    #         return super().form_valid(form)
    #     return HttpResponse("The user is an Employer and cannot apply for the position")


class MotivationLetterAppUserList(generic.ListView):
    model = MotivationLetter
    template_name = 'motivation_letter_list.html'
    context_object_name = 'letters'

    def get_queryset(self):
        letters = MotivationLetter.objects.filter(applicant_user__user__pk=self.request.user.id)
        if letters:
            return letters
        else:
            return []


class MotivationLetterAppDetails(generic.DetailView):
    model = MotivationLetter
    template_name = 'motivation_letter_details_app.html'
    context_object_name = 'letter'
