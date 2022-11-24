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
  path('shop/', views.ShopView.as_view(), name='shopPage'),
  path('orders/', views.OrdersView.as_view(), name='ordersPage'),
  path('product_detail/', views.ProductDetailView.as_view(), name='productDetailPage'),
  path('contact/', views.ContactView.as_view(), name='contactPage'),
  path('cart/', views.CartView.as_view(), name='cartPage'),
  path('confirmation/', views.ConfirmationView.as_view(), name='confirmationPage'),



 
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)














