from django.urls import path
from django.contrib.auth import views as auth_views

from authentication.views import CustomLoginView, CustomUserCreationView, CustomLogoutView,CustomPasswordChangeView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomUserCreationView.as_view(), name='register'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('change-password/success/', auth_views.PasswordChangeDoneView.as_view(), name='change_password_success'), 
]
