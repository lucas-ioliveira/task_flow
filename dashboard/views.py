import json
from django.shortcuts import render
from django.views import View

from tasks.repository import TaskRepository


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        user = request.user

        done = TaskRepository.get_tasks_by_status(None, user, 'Done')
        todo = TaskRepository.get_tasks_by_status(None, user, 'To do')
        in_progress = TaskRepository.get_tasks_by_status(None, user, 'In progress')
        paused = TaskRepository.get_tasks_by_status(None, user, 'Paused')

        priority_data = TaskRepository.get_tasks_grouped_by_priority(user)
        priority_labels = [item['priority'] for item in priority_data]
        priority_values = [item['total'] for item in priority_data]

        workspace_data = TaskRepository.get_tasks_grouped_by_workspace(user)
        workspace_labels = [item['work_space__title'] for item in workspace_data]
        workspace_values = [item['total'] for item in workspace_data]

        context = {
            'done': done,
            'todo': todo,
            'in_progress': in_progress,
            'paused': paused,
            'priority_labels': json.dumps(priority_labels),
            'priority_values': json.dumps(priority_values),
            'workspace_labels': json.dumps(workspace_labels),
            'workspace_values': json.dumps(workspace_values),
        }
        return render(request, self.template_name, context)
