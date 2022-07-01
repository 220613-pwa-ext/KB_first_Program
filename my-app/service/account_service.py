from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError

class AccountService:

    def __init__(self):

        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_account_by_customer_id(self, c_id):

        if self.customer_dao.get_customer_by_id(c_id) is None:
            raise CustomerNotFoundError(f"Customer with id {c_id} was not found")

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_account_by_customer_id(c_id)))

    def add_account(self, account_object):
        if not "chequing" or "saving" in account_object.account_type:
            raise InvalidParameterError("account type must be chequing or saving")

        if account_object.balance < 0:
            raise InvalidParameterError("balance must be at least 0 dollars")

        add_account_object = self.account_dao.add_account(account_object)
        return add_account_object.to_dict()
