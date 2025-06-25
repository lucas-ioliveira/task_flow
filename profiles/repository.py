from profiles.models import ContactDetails


class ProfileRepository:
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