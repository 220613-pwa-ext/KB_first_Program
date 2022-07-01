class Account:
    def __init__(self, account_id, balance, c_id, account_type, active):
        self.account_id = account_id
        self.balance = balance
        self.c_id = c_id
        self.active = active
        self.account_type = account_type

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "c_id": self.c_id,
            "account_type": self.account_type,
            "active": self.active
        }
