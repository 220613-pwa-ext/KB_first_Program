class User:
    def __init__(self, u_id,username, password, first_name, last_name, gender, phone_number, email_address, role):
        self.u_id = int(u_id)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.email_address = email_address
        self.role = role

    def to_dict(self):
        return {
            "u_id": self.u_id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "gender": self.gender,
            "email_address": self.email_address,
            "role": self.role
        }
