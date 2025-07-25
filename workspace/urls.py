from django.urls import path

from workspace.views import WorkSpaceView, WorkSpaceEditarView, WorkSpaceDeletarView


urlpatterns = [
    path('', WorkSpaceView.as_view(), name='work-space'),
    path('<int:work_space_id>/update/', WorkSpaceEditarView.as_view(), name='work-space-update'),
    path('<int:work_space_id>/delete/', WorkSpaceDeletarView.as_view(), name='work-space-delete'),
]
