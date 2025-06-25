from workspace.models import WorkSpace


class WorkSpaceRepository:
    @staticmethod
    def get_all_work_space(user):
        try:
            return WorkSpace.objects.filter(user=user, active=True).order_by('created_at')
        except:
            return None
    
    @staticmethod
    def get_work_space_by_id(id):
        try:
            return WorkSpace.objects.get(id=id)
        except:
            return None
        
    @staticmethod
    def get_work_space_title_by_id(id):
        try:
            return WorkSpace.objects.get(id=id).title
        except:
            return None
    
    @staticmethod
    def create_work_space(title, user):
        try:
            work_space = WorkSpace.objects.create(title=title, user=user)
            return work_space
        except:
            return None
    
    @staticmethod
    def update_work_space(id, title):
        try:
            work_space = WorkSpaceRepository.get_work_space_by_id(id)
            work_space.title = title
            work_space.save()
            return work_space
        except:
            return None
    @staticmethod
    def delete_work_space_by_id(id):
        try:
            work_space = WorkSpaceRepository.get_work_space_by_id(id)
            work_space.active = False
            work_space.save()
            return work_space
        except:
            return None