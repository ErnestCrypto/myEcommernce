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

    












