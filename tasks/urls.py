from django.urls import path
from tasks.views import TasksListView


urlpatterns = [
    path('<work_space_id>/', TasksListView.as_view(), name='tasks'),
]
