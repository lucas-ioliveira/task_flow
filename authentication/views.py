from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from authentication.service import AuthenticationService


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        previous_page = request.META.get("HTTP_REFERER")
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username, password]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect(previous_page)
        
        user = auth.authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, "Usuário ou senha inválidos!")
            return redirect(previous_page)
        
        auth.login(request, user)
        messages.success(request, "Bem-vindo!")
        return redirect(self.success_url)
        

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class CustomUserCreationView(View):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login') 

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        previous_page = request.META.get("HTTP_REFERER")
        
        response = AuthenticationService.create_user(request)
        if response["error"]:
            messages.error(request, response["message"])
            return redirect(previous_page)

        messages.success(request, response["message"])
        return redirect(self.success_url)


method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'profile.html' 
    success_url = reverse_lazy('profile') 
    
    def form_valid(self, form):
        messages.success(self.request, "Sua senha foi alterada com sucesso!")
        return super().form_valid(form)