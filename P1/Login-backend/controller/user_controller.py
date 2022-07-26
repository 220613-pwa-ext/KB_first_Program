from flask import Blueprint, request, session

from exception.login import LoginException
from exception.registration import RegistrationException
from model.user import User
from services.user_service import UserService

uc = Blueprint("user_controller", __name__)
user_service = UserService()


@uc.route('/loginstatus', methods=['GET'])
def loginstatus():
    if session.get('user_info') is not None:
        return {
            "message": "You are logged in",
            "logged_in_user": session.get('user_info')
        }, 200
    else:
        return {
            "message": "You are not logged in"
        }, 200

@uc.route('/logout', methods=['POST'])
def logout():
    session.clear()

    return {
        "message": "Logged out Successfully"
    }, 200

@uc.route('/login', methods=['POST'])
def login():
    request_body_dict = request.get_json()

    username = request_body_dict['username']
    password = request_body_dict['password']

    try:
        user_dict = user_service.login(username, password)

        # We add a key to the Http session object called 'user_info' that contains the dictionary
        # with all of the user information
        # Any subsequent request that is made by the client will be identified with the appropriate Http session
        # object that contains that key
        session['user_info'] = user_dict

        return user_dict, 200
    except LoginException as e:
        return {
            "message": str(e)
        }, 400



@uc.route('/users', methods=['POST'])
def add_user():
    request_body_dict = request.get_json()

    username = request_body_dict.get('username')
    password = request_body_dict.get('password')
    first_name = request_body_dict.get('first_name')
    last_name = request_body_dict.get('last_name')
    gender = request_body_dict.get('gender')
    phone_number = request_body_dict.get('phone_number')
    email_address = request_body_dict.get('email_address')
    role = request_body_dict.get('role')

    try:
        added_user = user_service.add_user(User(None, username, password, first_name, last_name, gender, phone_number,
                                                email_address, role))
    except RegistrationException as e:
        return {
            "messages": e.messages
        }, 400

    return added_user, 200


@uc.route('/employee_reimbs/<u_id>')
def get_reimb_by_employee_id(u_id):
    try:
        user = user_service.get_reimb_by_employee_id(int(u_id))
    except RegistrationException as e:
        return {
            "messages": e.messages
        }, 400
    if user is None:
        user_r = user_service.get_reimb_by_manager_id(u_id)
        return {
                   "reimbs": user_r
               }, 200
    return {
              "reimbs": user
           }, 200