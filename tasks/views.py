from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from tasks.service import TasksServices
from tasks.repository import TaskRepository
from workspace.repository import WorkSpaceRepository


@method_decorator(login_required, name='dispatch')
class TasksListView(View):
    template_name = 'tasks/tasks.html'
    def get(self, request, work_space_id):
        work_space = WorkSpaceRepository.get_all_work_space(request.user)
        work_space_name = WorkSpaceRepository.get_work_space_title_by_id(work_space_id)

        status = TaskRepository.get_status_choices()
        priority = TaskRepository.get_priority_choices()

        done = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'Done')
        todo = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'To do')
        in_progress = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'In progress')
        paused = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'Paused')

        context = {
            'work_space': work_space,
            'work_space_name': work_space_name,
            'work_space_id': work_space_id,
            'status': status,
            'priority': priority,
            'done': done,
            'todo': todo,
            'in_progress': in_progress,
            'paused': paused,
            
        }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class TaskCreateView(View):

    def post(self, request):
        previous_page = request.META.get("HTTP_REFERER")
        data = {
            'work_space_id': request.POST.get('work_space_id'),
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'priority': request.POST.get('priority'),
            'user': request.user
        }
        task = TasksServices.create_task(data)
        if not task:
            messages.error(request, 'Ocorreu um erro ao criar a tarefa!')
            return redirect(previous_page)
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect(previous_page)