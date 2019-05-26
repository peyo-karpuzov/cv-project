from django.db import models
from django.contrib.auth.models import User


class JobOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    starting_salary = models.PositiveIntegerField()
    job_description = models.TextField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company_name} company - {self.position} position."
