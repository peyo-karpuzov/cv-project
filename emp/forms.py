from django import forms
from . import models


class EmployerUserForm(forms.ModelForm):
    company_name = forms.CharField(required=True)

    class Meta:
        model = models.EmployerUser
        fields = ('company_name',)


class JobOfferCreate(forms.ModelForm):
    position = forms.CharField(required=True)
    starting_salary = forms.IntegerField(required=True)
    job_description = forms.CharField(required=True, widget=forms.Textarea)
    address = forms.CharField(required=True)

    class Meta:
        model = models.JobOffer
        fields = ('id', 'address', 'position', 'starting_salary', 'job_description',)
