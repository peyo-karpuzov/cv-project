from django import forms
from django.core.validators import RegexValidator, URLValidator

from . import models
from . import fill_in_choices


class ApplicantUserForm(forms.ModelForm):
    name_first = forms.CharField(required=True,
                                 validators=[RegexValidator(
                                     r'^[A-Z][a-z]+$', message="Start name with a capital letter and use only letters")],
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    name_last = forms.CharField(required=True,
                                validators=[RegexValidator(
                                     r'^[A-Z][a-z]+$', message="Start name with a capital letter and use only letters.")],
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.ApplicantUser
        fields = ('id', 'name_first', 'name_last',)


class CVGeneralForm(forms.ModelForm):
    town = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    pic = forms.URLField(required=True,
                         validators=[URLValidator(message="You need to add a valid URL.")],
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    email = forms.CharField(required=True,
                            validators=[RegexValidator(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                                                       message="Enter valid email.")],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(required=True, max_length=3,
                             widget=forms.Select(choices=fill_in_choices.GENDER, attrs={'class': 'form-control'}))

    class Meta:
        model = models.CVGeneral
        fields = ('id', 'street', 'town', 'pic', 'phone_number', 'email', 'gender',)


class CVWorkplaceForm(forms.ModelForm):
    company = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))
    end_date = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control'}))
    cv_general = forms.ModelChoiceField(required=True, queryset=models.CVGeneral.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.CVWorkPlaces
        fields = ('id', 'company', 'position', 'start_date', 'end_date', 'cv_general')


class CVEducationForm(forms.ModelForm):
    degree = forms.CharField(required=True,
                             max_length=3,
                             widget=forms.Select(choices=fill_in_choices.EDUCATION_TYPES,
                                                 attrs={'class': 'form-control'}))
    institution = forms.CharField(required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))
    end_date = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control'}))
    cv_general=forms.ModelChoiceField(required=True,
                                      queryset=models.CVGeneral.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.CVEducation
        fields = ('id', 'degree', 'institution', 'start_date', 'end_date', 'cv_general')


class CVLanguagesForm(forms.ModelForm):
    language = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    writing = forms.CharField(required=True,
                              max_length=2,
                              widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY,
                                                  attrs={'class': 'form-control'}))
    speaking = forms.CharField(required=True,
                               max_length=2,
                               widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY,
                                                   attrs={'class': 'form-control'}))
    reading = forms.CharField(required=True,
                              max_length=2,
                              widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY,
                                                  attrs={'class': 'form-control'}))
    listening = forms.CharField(required=True,
                                max_length=2,
                                widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY,
                                                    attrs={'class': 'form-control'}))
    cv_general = forms.ModelChoiceField(required=True,
                                        queryset=models.CVGeneral.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.CVLanguages
        fields = ('id', 'language', 'writing', 'speaking', 'reading', 'listening', 'cv_general')


class MotivationLetterForm(forms.ModelForm):
    job_offer = forms.ModelChoiceField(required=True,
                                       queryset=models.JobOffer.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    cv_general = forms.ModelChoiceField(required=True,
                                        queryset=models.CVGeneral.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    text = forms.CharField(required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = models.MotivationLetter
        fields = ('id', 'job_offer', 'cv_general', 'text',)