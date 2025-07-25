from workspace.repository import WorkSpaceRepository


class WorkSpaceService:
    @staticmethod
    def create_work_space(data):
        try:
            title = data.get('title')
            user = data.get('user')
            return WorkSpaceRepository.create_work_space(title, user)
        except:
            return None
        
    @staticmethod
    def update_work_space(data):
        try:
            work_space_id = data.get('work_space_id')
            title = data.get('title')
            return WorkSpaceRepository.update_work_space(work_space_id, title)
        except:
            return None
        