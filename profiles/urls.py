from django.urls import path

from profiles.views import ProfileView, AddressView, AddressUpdateView, UserUpdateView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('address/', AddressView.as_view(), name='address-get'),
    path('address/update/', AddressUpdateView.as_view(), name='address-update'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
]