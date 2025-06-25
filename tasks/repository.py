from tasks.models import Task


class TaskRepository:
    @staticmethod
    def get_tasks_by_status(work_space_id=None, user=None, status=None):
        try:
            if work_space_id:
                return Task.objects.filter(
                    work_space_id=work_space_id, user=user, active=True, status=status
                    ).order_by('created_at')

            return Task.objects.filter(user=user, active=True, status=status).order_by('created_at')
        except Task.DoesNotExist:
            return None
        
    @staticmethod
    def get_status_choices():
        return Task.STATUS_CHOICES
    
    @staticmethod
    def get_priority_choices():
        return Task.PRIORITY_CHOICES
    
    @staticmethod
    def create_task(work_space_id, title, description, status, priority, user):
        try:
            task = Task.objects.create(
                work_space_id=work_space_id,
                title=title,
                description=description,
                status=status,
                priority=priority,
                user=user
            )
            return task
        except:
            return None
    
    @staticmethod
    def update_status_task(id, status, completed_at=None):
        try:
            task = Task.objects.get(id=id)
            task.status = status
            if completed_at is not None:
                task.completed_at = completed_at
            task.save()
            return task
        except Task.DoesNotExist:
            return None