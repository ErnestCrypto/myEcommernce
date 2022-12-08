from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'dashboard_index.html'

    def post(self, request):
        if request.method == 'POST':
            return render(request, 'dashboard_index.html')

    def get(self, request):
        return render(request, 'dashboard_index.html')

class AddProductView(TemplateView):
    template_name = 'add_product.html'
    

class ProductListView(TemplateView):
    template_name = 'product_list.html'


class orderListView(TemplateView):
    template_name = 'order_list.html'
