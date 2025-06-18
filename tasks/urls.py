from django.urls import path
from tasks.views import TasksListView, TaskCreateView


urlpatterns = [
    path('<int:work_space_id>/', TasksListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
]
