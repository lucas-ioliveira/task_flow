from django.shortcuts import render
from django.views import View

from workspace.service import WorkSpaceRepository
from tasks.repository import TaskRepository


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        work_space = WorkSpaceRepository.get_all_work_space(request.user)

        done = TaskRepository.get_tasks_by_status(None, request.user, 'Done')
        todo = TaskRepository.get_tasks_by_status(None, request.user, 'To do')
        in_progress = TaskRepository.get_tasks_by_status(None, request.user, 'In progress')
        paused = TaskRepository.get_tasks_by_status(None, request.user, 'Paused')

        context = {
            'work_space': work_space,
            'done': done,
            'todo': todo,
            'in_progress': in_progress,
            'paused': paused
        }
        return render(request, self.template_name, context)
