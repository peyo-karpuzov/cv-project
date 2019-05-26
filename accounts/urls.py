from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('logout/', views.redirect_to_login_page, name='redirect-to-login'),
    path('profile/', views.redirect_to_common_profile, name='redirect-to-common-profile'),
    re_path('^profile/common/(?P<pk>\d+)/$', views.CommonProfile.as_view(), name='common-profile'),
    path('password_change/done/', views.redirect_to_login_page),
    #path('landing/', name='landing'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register-user')
]