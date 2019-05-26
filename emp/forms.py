from django import forms
from django.core.validators import MinValueValidator

from . import models


class JobOfferForm(forms.ModelForm):
    company_name = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    starting_salary = forms.IntegerField(required=True,
                                         validators=[MinValueValidator(520,
                                                                       message="Minimum national salary is 520.")],
                                         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    job_description = forms.CharField(required=True,
                                      widget=forms.Textarea(attrs={'class': 'form-control'}))
    address = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.JobOffer
        fields = ('id', 'company_name', 'address', 'position', 'starting_salary', 'job_description',)


# class EmployerUserForm(forms.ModelForm):
#     company_name = forms.CharField(required=True)
#
#     class Meta:
#         model = models.EmployerUser
#         fields = ('company_name',)