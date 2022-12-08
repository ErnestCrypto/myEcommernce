from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = "dashboardUrls"

urlpatterns=[
    path('',views.IndexView.as_view(),name='indexPage'),
    path('add_product/', views.AddProductView.as_view(), name='addProductPage'),
    path('product_list/', views.ProductListView.as_view(), name='productListPage'),
    path('order_list/', views.orderListView.as_view(), name='orderListPage'),
    path('order_details/', views.orderDetailsView.as_view(), name='orderDetailsPage'),




]

urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)

