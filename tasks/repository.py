from tasks.models import Task


class TaskRepository:
    @staticmethod
    def get_tasks_by_status(work_space_id, user, status):

        return Task.objects.filter(
            work_space_id=work_space_id, user=user, active=True, status=status
            ).order_by('created_at')
        
