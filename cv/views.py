from django.shortcuts import render
from django.views import generic
from . import models


class MotivationLetterDetails(generic.DetailView):
    model = models.MotivationLetter
    template_name = 'motivation_letter_details.html'
    context_object_name = 'letter'

