from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'
    
   

class SignupView(TemplateView):
    template_name = 'signup.html'


class Forget_PasswordView(TemplateView):
    template_name = 'forget_password.html'


class IndexView(TemplateView):
    template_name = 'index.html'
   
    def post(self,request):
        if request.method == 'POST':
            return render(request, 'index.html')
    def get(self,request):
        return render(request, 'index.html')
        

class ShopView(TemplateView):
    template_name = 'shop.html'

    

class OrdersView(TemplateView):
    template_name = 'orders.html'
    
   
class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'











