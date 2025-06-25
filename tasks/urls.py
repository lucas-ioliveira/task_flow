from django.urls import path
from tasks.views import TasksListView, TaskCreateView, TaskUpdateStatusView


urlpatterns = [
    path('<int:work_space_id>/', TasksListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:task_id>/update/', TaskUpdateStatusView.as_view(), name='task-update-status'),
]
