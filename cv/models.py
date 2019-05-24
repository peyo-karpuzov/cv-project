from django.db import models
from django.contrib.auth.models import User

from emp.models import JobOffer

from . import fill_in_choices


class ApplicantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_first = models.CharField(max_length=20)
    name_last = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name_first} {self.name_last}"


class CVGeneral(models.Model):
    town = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    pic = models.URLField()
    phone_number = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=fill_in_choices.GENDER)
    applicant_user = models.ForeignKey(ApplicantUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"General Info about {self.applicant_user}"


class CVWorkPlaces(models.Model):
    company = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    cv_general = models.ForeignKey(CVGeneral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Work place: {self.position} in {self.company}"


class CVEducation(models.Model):
    degree = models.CharField(max_length=3, choices=fill_in_choices.EDUCATION_TYPES)
    institution = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    cv_general = models.ForeignKey(CVGeneral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Education: {self.get_degree_display}"


class CVLanguages(models.Model):
    language = models.CharField(max_length=20)
    writing = models.CharField(max_length=2, choices=fill_in_choices.LANGUAGE_PROFICIENCY)
    speaking = models.CharField(max_length=2, choices=fill_in_choices.LANGUAGE_PROFICIENCY)
    reading = models.CharField(max_length=2, choices=fill_in_choices.LANGUAGE_PROFICIENCY)
    listening = models.CharField(max_length=2, choices=fill_in_choices.LANGUAGE_PROFICIENCY)
    cv_general = models.ForeignKey(CVGeneral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Language: {self.language}"


class MotivationLetter(models.Model):
    applicant_user = models.ForeignKey(ApplicantUser, on_delete=models.CASCADE)
    job_offer = models.OneToOneField(JobOffer, on_delete=models.CASCADE)
    cv_general = models.ForeignKey(CVGeneral, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.applicant_user} applying for {self.job_offer.position}"
