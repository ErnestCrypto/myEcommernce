from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = "dashboardUrls"

urlpatterns=[
    path('',views.IndexView.as_view(),name='indexPage'),
    path('add_product/', views.AddProductView.as_view(), name='addProductPage'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)

