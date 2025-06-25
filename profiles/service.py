import requests
import re
from profiles.repository import ProfileRepository


class ProfileService:
    @staticmethod
    def get_address(request):
        try:
            cep = re.sub(r'\D', '', request.GET.get("cep"))
        except Exception:
            raise Exception("CEP inválido.")

        url = f'https://cep.awesomeapi.com.br/json/{cep}'
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            address_dict = {
                'address': data.get('address', ''),
                'district': data.get('district', ''),
                'city': data.get('city', ''),
                'uf': data.get('state', ''),
            }
            return address_dict
        else:
            raise Exception(f"Erro externo: {response.status_code} - {response.text}")
    
    @staticmethod
    def update_address(data):
        try:

            user = data.get('user')
            phone = re.sub(r'\D', '', data.get('phone'))
            cep = re.sub(r'\D', '', data.get('cep'))
            address = data.get('address')
            number_address = data.get('number_address')
            district = data.get('district')
            city = data.get('city')
            state = data.get('state')
            complement = data.get('complement')
            return ProfileRepository.update_address(user, phone, cep, address, number_address, district, city, state, complement)
        except:
            return None