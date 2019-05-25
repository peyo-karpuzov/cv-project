from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^home/(?P<pk>\d+)/$', views.ApplicantProfile.as_view(), name='applicant-profile'),
    re_path('^motivation_letters/(?P<pk>\d+)/$', views.MotivationLetterDetails.as_view(), name='mot_letter_details'),
    path('applicant/create/', views.ApplicantCreate.as_view(), name='applicant-create'),
    path('general/create/', views.CVGeneralCreate.as_view(), name='cv-general-create'),
    path('workplace/create/', views.CVWorkplaceCreate.as_view(), name='cv-workplace-create'),
    path('education/create/', views.CVEducationCreate.as_view(), name='cv-education-create'),
    path('language/create/', views.CVLanguagesCreate.as_view(), name='cv-languages-create'),
    path('my_cvs/', views.CVList.as_view(), name='cv-all'),
    path('my_cvs/mine/', views.CVUserList.as_view(), name='cv-mine'),
    re_path('^my_cvs/(?P<pk>\d+)/$', views.CVDetails.as_view(), name='cv-details'),
    re_path('my_cvs/edit/(?P<pk>\d+)/$', views.CVEdit.as_view(), name='cv-edit'),
    re_path('my_cvs/delete/(?P<pk>\d+)/$', views.CVDelete.as_view(), name='cv-delete'),
    path('send_letter/', views.SendLetterCreate.as_view(), name='letter-create'),
]