from django.shortcuts import render
from django.views import View

from workspace.service import WorkSpaceRepository


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        work_space = WorkSpaceRepository.get_all_work_space(request.user)
        context = {
            'work_space': work_space
        }
        return render(request, self.template_name, context)
