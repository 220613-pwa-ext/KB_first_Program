from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

cc = Blueprint('customer_controller', __name__)


customer_service = CustomerService()




@cc.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }


@cc.route('/customers/<c_id>')
def get_customer_by_id(c_id):
    try:
        return customer_service.get_customer_by_id(c_id)
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@cc.route('/customers/<c_id>', methods=['DELETE'])
def delete_customer_by_id(c_id):
    try:
        customer_service.delete_customer_by_id(c_id)

        return {
            "message": f"Customer with id {c_id} was successfully deleted"
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@cc.route('/customers', methods=['POST'])
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['c_name'], customer_json_dictionary['last_name'], customer_json_dictionary['p_word'],
                               customer_json_dictionary['e_mail'], customer_json_dictionary['gender'])
    try:
        return customer_service.add_customer(customer_object), 201

    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


@cc.route('/customers/<c_id>', methods=['PUT'])
def update_customer_by_id(c_id):
    try:
        json_dictionary = request.get_json()
        return customer_service.update_customer_by_id(Customer(c_id, json_dictionary['c_name'], json_dictionary['last_name'],
                                                   json_dictionary['p_word'], json_dictionary['e_mail'], json_dictionary['gender']))
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


