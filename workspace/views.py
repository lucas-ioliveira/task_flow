from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from workspace.service import WorkSpaceService
from workspace.repository import WorkSpaceRepository


@method_decorator(login_required, name='dispatch')
class WorkSpaceView(View):

    def post(self, request):
        data = {
            'title': request.POST.get('title'),
            'user': request.user
        }
        work_space = WorkSpaceService.create_work_space(data)
        if not work_space:
            messages.error(request, 'Ocorreu um erro ao criar o espaço de trabalho!')
            return redirect('dashboard')
        messages.success(request, 'Espaço de trabalho criado com sucesso!')
        return redirect('dashboard')

@method_decorator(login_required, name='dispatch')
class WorkSpaceEditarView(View):

    def post(self, request, work_space_id):
        data = {
            'work_space_id': work_space_id,
            'title': request.POST.get('titulo_update'),
            'user': request.user
        }
        work_space = WorkSpaceService.update_work_space(data)
        if not work_space:
            messages.error(request, 'Ocorreu um erro ao editar o espaço de trabalho!')
            return redirect('dashboard')
        messages.success(request, 'Espaço de trabalho editado com sucesso!')
        return redirect('dashboard')
    
@method_decorator(login_required, name='dispatch')
class WorkSpaceDeletarView(View):
    def post(self, request, work_space_id):
        work_space = WorkSpaceRepository.delete_work_space_by_id(work_space_id)
        if not work_space:
            messages.error(request, 'Ocorreu um erro ao deletar o espaço de trabalho!')
            return redirect('dashboard')
        messages.success(request, 'Espaço de trabalho deletado com sucesso!')
        return redirect('dashboard')