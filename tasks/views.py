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
        done = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'Done')
        todo = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'To Do')
        in_progress = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'In Progress')
        paused = TaskRepository.get_tasks_by_status(work_space_id, request.user, 'Paused')

        context = {
            'done': done,
            'todo': todo,
            'in_progress': in_progress,
            'paused': paused,
            'work_space': work_space,
            'work_space_name': work_space_name
        }
        return render(request, self.template_name, context)

