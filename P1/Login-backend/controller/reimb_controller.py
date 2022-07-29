from flask import Blueprint
from exception.registration import RegistrationException
from exception.reimbnotfound import ReimbNotFoundException
from services.reimb_service import ReimbService

rc = Blueprint("reimb_controller", __name__)
reimb_service = ReimbService()


@rc.route('/employee_reimbs/<u_id>')
def get_reimb_by_employee_id(u_id):
    try:
        reimb = reimb_service.get_reimb_by_employee_id(int(u_id))
    except RegistrationException as e:
        return {
            "messages": e.messages
        }, 400
    if reimb is None:
        user_r = reimb_service.get_reimb_by_manager_id(u_id)
        return {
                   "reimbs": user_r
               }, 200
    return {
              "reimbs": reimb
           }, 200


@rc.route('/employee_reimbs/<reimb_id>/<stat>', methods=['PUT'])
def update_reimb_by_id(reimb_id, stat):
    try:
        reimb = reimb_service.update_reimb_by_id(reimb_id, stat)
        return reimb
    except ReimbNotFoundException as e:
        return {
            "message": str(e)
        }, 404