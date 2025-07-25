from django.contrib import auth
from django.core.validators import validate_email

from authentication.repository import AuthenticationRepository

class AuthenticationService:

    @staticmethod
    def login_user(request):
        response = {
            "error": False,
            "message": ""
        }

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username, password]):
            response["error"] = True
            response["message"] = "Todos os campos são obrigatórios."
            return response

        user = auth.authenticate(request, username=username, password=password)
        if not user:
            response["error"] = True
            response["message"] = "Usuário ou senha inválidos!"
            return response

        auth.login(request, user)
        response["error"] = False
        response["message"] = "Bem-vindo!"
        return response

    @staticmethod
    def create_user(request):
        response = {
            "error": False,
            "message": ""
        }

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([first_name, last_name, username, email, password, password2]):
            response["error"] = True
            response["message"] = "Todos os campos são obrigatórios."
            return response

        if AuthenticationRepository.get_user_by_username(username):
            response["error"] = True
            response["message"] = "Nome de usuário indisponível!"
            return response

        try:
            validate_email(email)
        except:
            response["error"] = True
            response["message"] = "E-mail inválido!"
            return response

        if AuthenticationRepository.get_user_by_email(email):
            response["error"] = True
            response["message"] = "E-mail já existe!"
            return response

        if len(password) < 8:
            response["error"] = True
            response["message"] = "Senha precisa ter no mínimo 8 caracteres!"
            return response

        if password != password2:
            response["error"] = True
            response["message"] = "Senhas diferentes!"
            return response

        AuthenticationRepository.create_user(first_name, last_name, email, username, password)
        response["error"] = False
        response["message"] = "Usuário cadastrado com sucesso!"

        return response

