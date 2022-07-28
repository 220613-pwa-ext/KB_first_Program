import re
from dao.user_dao import UserDao
from exception.login import LoginException
from exception.user import UserException
from exception.registration import RegistrationException
from exception.usernotfound import UserNotFoundException


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def login(self, username, password):
        user_obj = self.user_dao.get_user_by_username_password(username, password)

        if user_obj is None:
            raise LoginException("Invalid username and/or password")
        else:
            return user_obj.to_dict()

    def add_user(self, user_object):

        registration_exception = RegistrationException()

        #Check username for valid test cases
        if user_object.username =='':
            registration_exception.messages.add("Username cannot be blank!")

        if len(user_object.username) < 4 or len(user_object.username) > 20:
            registration_exception.messages.add("Username cannot be less than 4 or greater than 20!")

        if user_object.username.isalnum() is False:
            registration_exception.messages.add("Username must be alphanumeric!")

        if self.user_dao.get_user_by_username(user_object.username) is not None:
            registration_exception.messages.add("Username is already taken!")

        # Check password for valid test cases
        alphabetical_characters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "!@#$%^&*()_+{}[],./<>?;':"""
        numeric_characters = "0123456789"

        lalpha_count = 0
        ualpha_count = 0
        special_character_count = 0
        numeric_character_count = 0

        for char in user_object.password:
            if char in alphabetical_characters:
                lalpha_count +=1
            if char in alphabetical_characters.upper():
                ualpha_count +=1
            if char in special_characters:
                special_character_count += 1
            if char in numeric_characters:
                numeric_character_count +=1

        if lalpha_count == 0:
            registration_exception.messages.add("Password needs to contain minimum 1 lowercase character")
        if ualpha_count == 0:
            registration_exception.messages.add("Password needs to contain minimum 1 uppercase character")
        if special_character_count == 0:
            registration_exception.messages.add("Password needs to contain minimum 1 special character")
        if numeric_character_count == 0:
            registration_exception.messages.add("Password needs to contain minimum 1 numeric character")
        if user_object.password =='':
            registration_exception.messages.add("Password cannot be blank!")
        if len(user_object.password) < 6 or len(user_object.password) > 26:
            registration_exception.messages.add("Password cannot be less than 6 or greater than 26!")
        if len(user_object.password) != lalpha_count+ualpha_count+special_character_count+numeric_character_count:
            registration_exception.messages.add("Password must only contain alphanumeric and special characters")

        # Check firstname for valid test cases

        special_character_count_name = 0
        numeric_character_count_name = 0

        for char in user_object.first_name:
            if char in special_characters:
                special_character_count_name += 1
            if char in numeric_characters:
                numeric_character_count_name += 1

        if user_object.first_name.isalpha() is not True:
            registration_exception.messages.add("First name can only contain alphabetical characters")
        if len(user_object.first_name) < 3 or len(user_object.first_name) > 40:
            registration_exception.messages.add("First name cannot be less than 3 or greater than 40!")
        if user_object.first_name[0].isupper() is not True:
            registration_exception.messages.add("First name must have first letter uppercase!")
        if special_character_count_name == 0:
            registration_exception.messages.add("first name must only contain alphabetical characters")
        if numeric_character_count_name == 0:
            registration_exception.messages.add("first name must only contain alphabetical characters")

            # Check lastname for valid test cases

            special_character_count_lname = 0
            numeric_character_count_lname = 0

            for char in user_object.last_name:
                if char in special_characters:
                    special_character_count_lname += 1
                if char in numeric_characters:
                    numeric_character_count_lname += 1

            if len(user_object.last_name) > 40:
                registration_exception.messages.add("Last name cannot be greater than 40!")
            if special_character_count_lname == 0:
                registration_exception.messages.add("Last name must only contain alphabetical characters")
            if numeric_character_count_lname == 0:
                registration_exception.messages.add("Last name must only contain alphabetical characters")

            # Check email for valid test cases

            if user_object.email_address is None:
                registration_exception.messages.add("Email-address is already taken!")
            if len(user_object.email_address) > 30:
                registration_exception.messages.add("Email-address must be less than 30 characters!")
            if not re.fullmatch("\[a-zA-Z0-9_.-]+@[a-z]+.[a-z]+", user_object.email_address):
                registration_exception.messages.add("Email-address must be of form <username>@<domain>!")

            # Check Gender for valid test cases
            if not (user_object.gender == "male" or user_object.gender == "female" or user_object.gender == "other"):
                registration_exception.messages.add("Gender must be male female or other!")

            # Check Role for valid test cases
            if not (user_object.role == "employee" or user_object.role == "finance_manager"):
                registration_exception.messages.add("Role must be employee or finance_manager!")

            # Check Phone number for valid test cases

            if not re.fullmatch("\[0-9]{3}-[0-9]{3}-[0-9]{4}", user_object.phone_number):
                registration_exception.messages.add("Phone_number must be of form 000-000-0000!")

            if len(registration_exception.messages) > 0:
                raise registration_exception

            added_user_object = self.user_dao.add_user(user_object)

            return added_user_object.to_dict()

    def get_reimb_by_employee_id(self, u_id):
        list_of_reimbs = self.user_dao.get_reimb_by_employee_id(u_id)

        list_of_reimbs_dictionary = []

        if not list_of_reimbs:
            return None
        else:
            for reimbs in list_of_reimbs:
                list_of_reimbs_dictionary.append(reimbs.to_dict())
            return list_of_reimbs_dictionary

    def get_reimb_by_manager_id(self, u_id):
        list_of_reimbs = self.user_dao.get_reimb_by_manager_id(u_id)

        list_of_reimbs_dictionary = []

        if not list_of_reimbs:
            return None
        else:
            for reimbs in list_of_reimbs:
                list_of_reimbs_dictionary.append(reimbs.to_dict())
            return list_of_reimbs_dictionary


    def update_reimb_by_id(self, reimb_id, stat):
        update_reimb_object = self.user_dao.update_reimb_by_id(reimb_id, stat)

        if update_reimb_object is None:
            raise UserNotFoundException(f"Customer with id {reimb_id} was not found")

        return update_reimb_object.to_dict()
