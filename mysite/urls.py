# writing our urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "mysiteUrls"



urlpatterns = [
  path('', views.IndexView.as_view(), name='indexPage'),
  path('login/',views.LoginView.as_view(), name='loginPage'),
  path('signup/',views.SignupView.as_view(), name='signupPage'),
  path('forget_password/', views.Forget_PasswordView.as_view(), name='forget_passwordPage'),


  
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)














