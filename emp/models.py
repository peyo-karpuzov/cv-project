from django.db import models
from django.contrib.auth.models import User


class EmployerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user}, director of '{self.company_name}' company"


class JobOffer(models.Model):
    employer_user = models.ForeignKey(EmployerUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    starting_salary = models.PositiveIntegerField()
    job_description = models.TextField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employer_user.company_name} offers {self.position}"
