from django.contrib.auth.models import User
from profiles.models import ContactDetails


class ProfileRepository:

    @staticmethod
    def get_user_by_id(id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_contact_details(user):
        try:
            contact_details = ContactDetails.objects.get(user=user)
            return contact_details
        except ContactDetails.DoesNotExist:
            return None
    
    @staticmethod
    def create_contact_details(user, phone, cep, address, number_address, district, city, state, complement):

        try:
            contact_details = ContactDetails.objects.create(
                user=user,
                phone=phone,
                cep=cep,
                address=address,
                number_address=number_address,
                district=district,
                city=city,
                state=state,
                complement=complement
            )
            return contact_details
        except:
            return None
    
    @staticmethod
    def update_address(user, phone, cep, address, number_address, district, city, state, complement):
        try:

            contact_details = ProfileRepository.get_contact_details(user)
            if not contact_details:
                return ProfileRepository.create_contact_details(user, phone, cep, address, 
                                                         number_address, district, city, state, complement)

            contact_details.phone = phone
            contact_details.cep = cep
            contact_details.address = address
            contact_details.number_address = number_address
            contact_details.district = district
            contact_details.city = city
            contact_details.state = state
            contact_details.complement = complement
            contact_details.save()
            return contact_details
        except ContactDetails.DoesNotExist:
            return None
    
    @staticmethod
    def update_user(user_id, first_name, last_name, email):
        try:
            user = ProfileRepository.get_user_by_id(user_id)
            if not user:
                return None
            
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return user
        except User.DoesNotExist:
            return None