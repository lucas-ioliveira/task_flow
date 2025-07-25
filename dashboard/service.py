from workspace.repository import WorkSpaceRepository


class DashboardService:
    @staticmethod
    def get_all_work_space(user):
        return WorkSpaceRepository.get_all_work_space(user)