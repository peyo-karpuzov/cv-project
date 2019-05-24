from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('logout/', views.redirect_to_login_page, name='redirect-to-login'),
    path('profile/', views.redirect_to_job_offers, name='redirect-to-jobs'),
    path('password_change/done/', views.redirect_to_login_page),
    #path('landing/', name='landing'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register-user')
]