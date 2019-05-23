from django.db import models
from django.contrib.auth.models import User

from emp.models import JobOffer


class ApplicantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wish = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.first_name} has the following wish {self.wish}."


class MotivationLetter(models.Model):
    applicant_user = models.ForeignKey(ApplicantUser, on_delete=models.CASCADE)
    job_offer = models.OneToOneField(JobOffer, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.applicant_user.user.first_name} applying for {self.job_offer.position}"