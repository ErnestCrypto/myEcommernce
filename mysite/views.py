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
        context = {
            'Home':'active',
            'Shop':'',
            'Orders':'',
            'Contact':'',
        }
        return render(request, 'index.html',context)
        

class ShopView(TemplateView):
    template_name = 'shop.html'

    def get(self, request):
        context = {
            'Home': '',
            'Shop': 'active',
            'Orders': '',
            'Contact': '',
        }
        return render(request, 'shop.html', context)
    

class OrdersView(TemplateView):
    template_name = 'orders.html'

    def get(self, request):
        context = {
            'Home': '',
            'Shop': '',
            'Orders': 'active',
            'Contact': '',
        }
        return render(request, 'orders.html', context)
   
class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'
    def get(self, request):
        context = {
        'Home': '',
            'Shop': 'active',
        'Orders': '',
        'Contact': '',
    }
        return render(request, 'product_detail.html', context)

class ContactView(TemplateView):
    template_name = 'contact.html'
    def get(self, request):
        context = {
        'Home': '',
        'Shop': '',
        'Orders': '',
            'Contact': 'active',
    }
        return render(request, 'contact.html', context)

class CartView(TemplateView):
    template_name = 'cart.html'

    def get(self, request):
        context = {
            'Home': '',
            'Shop': 'active',
            'Orders': '',
            'Contact': '',
        }
        return render(request, 'cart.html', context)

class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'
    def get(self, request):
        context = {
            'Home': '',
            'Shop': '',
            'Orders': 'active',
            'Contact': '',
        }
        return render(request, 'confirmation.html', context)

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get(self, request):
        context = {
            'Home': '',
            'Shop': 'active',
            'Orders': '',
            'Contact': '',
        }
        return render(request, 'checkout.html', context)










