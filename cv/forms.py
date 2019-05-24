from django import forms
from . import models


class ApplicantUserForm(forms.ModelForm):
    name_first = forms.CharField(required=True)
    name_last = forms.CharField(required=True)

    class Meta:
        model = models.ApplicantUser
        fields = ('name_first', 'name_last')