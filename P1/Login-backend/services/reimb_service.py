from dao.reimb_dao import ReimbDao
from exception.reimbnotfound import ReimbNotFoundException


class ReimbService:

    def __init__(self):
        self.reimb_dao = ReimbDao()

    def get_reimb_by_employee_id(self, u_id):
        list_of_reimbs = self.reimb_dao.get_reimb_by_employee_id(u_id)
        list_of_reimbs_dictionary = []
        if not list_of_reimbs:
            return None
        else:
            for reimbs in list_of_reimbs:
                list_of_reimbs_dictionary.append(reimbs.to_dict())
            return list_of_reimbs_dictionary

    def get_reimb_by_manager_id(self, u_id):
        list_of_reimbs = self.reimb_dao.get_reimb_by_manager_id(u_id)

        list_of_reimbs_dictionary = []

        if not list_of_reimbs:
            return None
        else:
            for reimbs in list_of_reimbs:
                list_of_reimbs_dictionary.append(reimbs.to_dict())
            return list_of_reimbs_dictionary

    def update_reimb_by_id(self, reimb_id, stat):
        update_reimb_object = self.reimb_dao.update_reimb_by_id(reimb_id, stat)

        if update_reimb_object is None:
            raise ReimbNotFoundException(f"Reimb with id {reimb_id} was not found")

        return update_reimb_object.to_dict()