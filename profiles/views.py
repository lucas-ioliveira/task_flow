from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from profiles.service import ProfileService
from profiles.repository import ProfileRepository
from workspace.service import WorkSpaceRepository

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'profiles/profiles.html'
    def get(self, request):
        contact_details = ProfileRepository.get_contact_details(request.user)
        if not contact_details:
            contact_details = None
        work_space = WorkSpaceRepository.get_all_work_space(request.user)

        context = {
            'work_space': work_space,
            'contact_details': contact_details
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        address = ProfileService.get_address(request)
        if not address:
            return JsonResponse({'address': None}, status=200)
        return JsonResponse({'address': address}, status=200)


@method_decorator(login_required, name='dispatch')
class AddressUpdateView(View):
    def post(self, request):
        previous_page = request.META.get("HTTP_REFERER")

        data = {
            'cep': request.POST.get('cep'),
            'address': request.POST.get('logradouro'),
            'number_address': request.POST.get('numero'),
            'district': request.POST.get('bairro'),
            'city': request.POST.get('cidade'),
            'state': request.POST.get('uf'),
            'complement': request.POST.get('complemento'),
            'phone': request.POST.get('telefone'),
            'user': request.user
        }

        address = ProfileService.update_address(data)
        if not address:
            messages.error(request, 'Ocorreu um  ao atualizar o endereço!')
            return redirect(previous_page)
        messages.success(request, 'Endereço atualizado com sucesso!')
        return redirect(previous_page)
