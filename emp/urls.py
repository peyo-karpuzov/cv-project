from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('employers/', views.EmployersList.as_view(), name='employers-all'),
    path('employers/create/', views.EmployerCreate.as_view(), name='employer-create'),
    re_path('^employers/(?P<pk>\d+)/$', views.EmployerDetails.as_view(), name='employer-details'),
    re_path('^employers/edit/(?P<pk>\d+)/$', views.EmployerEdit.as_view(), name='employer-edit'),
    re_path('^employer/delete/(?P<pk>\d+)/$', views.EmployerDelete.as_view(), name='employer-delete'),
    path('jobs/', views.JobOffersList.as_view(), name='jobs-all'),
    re_path('^jobs/(?P<pk>\d+)/$', views.JobOfferDetails.as_view(), name='job-details'),
    path('jobs/create/', views.JobOfferCreate.as_view(), name='job-create'),
    re_path('^jobs/edit/(?P<pk>\d+)/$', views.JobOfferEdit.as_view(), name='job-edit'),
    re_path('^jobs/delete/(?P<pk>\d+)/$', views.JobOfferDelete.as_view(), name='job-delete')
]