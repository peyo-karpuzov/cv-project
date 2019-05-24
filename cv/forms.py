from django import forms
from . import models
from . import fill_in_choices


class ApplicantUserForm(forms.ModelForm):
    name_first = forms.CharField(required=True)
    name_last = forms.CharField(required=True)

    class Meta:
        model = models.ApplicantUser
        fields = ('name_first', 'name_last')


class CVGeneralForm(forms.ModelForm):
    town = forms.CharField(required=True)
    street = forms.CharField(required=True)
    pic = forms.URLField()
    phone_number = forms.IntegerField(required=True)
    email = forms.CharField(required=True)
    gender = forms.CharField(required=True, max_length=3, widget=forms.Select(choices=fill_in_choices.GENDER))

    class Meta:
        model = models.CVGeneral
        fields = ('id', 'street', 'town', 'pic', 'phone_number', 'email', 'gender',)


class CVWorkplaceForm(forms.ModelForm):
    company = forms.CharField(required=True)
    position = forms.CharField(required=True)
    start_date = forms.DateField (required=True)
    end_date = forms.DateField(required=True)
    cv_general = forms.ModelChoiceField(required=True, queryset=models.CVGeneral.objects.all())

    class Meta:
        model = models.CVWorkPlaces
        fields = ('id', 'company', 'position', 'start_date', 'end_date', 'cv_general')


class CVEducationForm(forms.ModelForm):
    degree = forms.CharField(required=True, max_length=3, widget=forms.Select(choices=fill_in_choices.EDUCATION_TYPES))
    institution = forms.CharField(required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    cv_general=forms.ModelChoiceField(required=True, queryset=models.CVGeneral.objects.all())

    class Meta:
        model = models.CVEducation
        fields = ('id', 'degree', 'institution', 'start_date', 'end_date', 'cv_general')


class CVLanguagesForm(forms.ModelForm):
    language = forms.CharField(required=True)
    writing = forms.CharField(required=True, max_length=2, widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY))
    speaking = forms.CharField(required=True, max_length=2, widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY))
    reading = forms.CharField(required=True, max_length=2, widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY))
    listening = forms.CharField(required=True, max_length=2, widget=forms.Select(choices=fill_in_choices.LANGUAGE_PROFICIENCY))
    cv_general = forms.ModelChoiceField(required=True, queryset=models.CVGeneral.objects.all())

    class Meta:
        model = models.CVLanguages
        fields = ('id', 'language', 'writing', 'speaking', 'reading', 'listening', 'cv_general')
