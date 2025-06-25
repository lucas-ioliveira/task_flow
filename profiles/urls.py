from django.urls import path

from profiles.views import ProfileView, AddressView, AddressUpdateView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('address/', AddressView.as_view(), name='address-get'),
    path('address/update/', AddressUpdateView.as_view(), name='address-update'),
]