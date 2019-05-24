from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^motivation_letters/(?P<pk>\d+)/$', views.MotivationLetterDetails.as_view(), name='mot_letter_details'),
    path('applicant/create/', views.ApplicantCreate.as_view(), name='applicant-create')

]