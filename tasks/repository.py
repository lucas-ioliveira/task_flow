from django.db.models import Count

from tasks.models import Task


class TaskRepository:
    @staticmethod
    def get_tasks_by_status(work_space_id=None, user=None, status=None):
        filters = {
            'user': user,
            'active': True,
            'status': status,
            'work_space__active': True
        }

        if work_space_id:
            filters['work_space_id'] = work_space_id

        return Task.objects.filter(**filters).order_by('created_at')
        
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
    
    @staticmethod
    def update_task(id, title, description, priority, status, completed_at=None):
        try:
            task = Task.objects.get(id=id)
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            if completed_at is not None:
                task.completed_at = completed_at
            task.save()
            return task
        except Task.DoesNotExist:
            return None
    
    @staticmethod
    def delete_task(id):
        try:
            task = Task.objects.get(id=id)
            task.active = False
            task.save()
            return task
        except Task.DoesNotExist:
            return None
    
    @staticmethod
    def get_tasks_grouped_by_priority(user):
        return Task.objects.filter(
            user=user,
            active=True,
            work_space__active=True
        ).exclude(status='Done').values('priority').annotate(total=Count('id')).order_by('-total')

    @staticmethod
    def get_tasks_grouped_by_workspace(user):
        """Retorna a contagem de tarefas por Workspace"""
        return Task.objects.filter(
            user=user,
            active=True,
            work_space__active=True
        ).values('work_space__title').annotate(total=Count('id')).order_by('-total')