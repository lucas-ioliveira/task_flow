from django.contrib.auth.models import User


class AuthenticationRepository:

    @staticmethod
    def get_user_by_username(username):
        try:
            user = User.objects.get(username=username)
        except:
            return None
        return user

    @staticmethod
    def get_user_by_email(email):
        try:
            user = User.objects.get(email=email)
        except:
            return None
        return user

    @staticmethod
    def create_user(first_name, last_name, email, username, password):
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
        except:
            return None
        return user
