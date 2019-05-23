from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('employers/', views.EmployersList.as_view(), name='employers-all'),
    re_path('^employers/(?P<pk>\d+)/$', views.EmployerDetails.as_view(), name='employer-details'),
    path('jobs/', views.JobOffersList.as_view(), name='jobs-all'),
    re_path('^jobs/(?P<pk>\d+)/$', views.JobOfferDetails.as_view(), name='job-details')
]