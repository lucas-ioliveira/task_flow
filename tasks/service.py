from django.utils import timezone
from tasks.repository import TaskRepository

class TasksServices:
    @staticmethod
    def create_task(data):
        try:
            work_space_id = data.get('work_space_id')
            title = data.get('title')
            description = data.get('description')
            status = data.get('status')
            priority = data.get('priority')
            user = data.get('user')

            return TaskRepository.create_task(work_space_id, title, description, status, priority, user)
        except:
            return None

    @staticmethod
    def update_status_task(data):
        try:
            task_id = data.get('task_id')
            status = data.get('status')
            if status == 'Done':
                completed_at = timezone.now()
                return TaskRepository.update_status_task(task_id, status, completed_at)
            return TaskRepository.update_status_task(task_id, status)
        except:
            return None
