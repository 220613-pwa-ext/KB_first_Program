from flask import Blueprint, request
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from service.account_service import AccountService
from model.account import Account

ac = Blueprint('account_controller', __name__)



account_service = AccountService()


@ac.route('/customers/<c_id>/accounts')
def get_all_account_by_customer_id(c_id):
    accounts = account_service.get_all_account_by_customer_id(c_id)
    saving_account=[]
    chequing_account=[]
    for i in accounts:
        if(i["account_type"]=="saving"):
            saving_account.append(i)
        else:
            chequing_account.append(i)
    try:
        return {
            "chequing_accounts": chequing_account,
            "saving_accounts": saving_account
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@ac.route('/customers/<c_id>/accounts/<account_id>')
def get_account_by_customer_id_and_account_id(c_id, account_id):
    pass


@ac.route('/customers/<c_id>/accounts', methods=['POST'])
def add_account_for_customer_by_customer_id(c_id):
    account_json_dictionary = request.get_json()
    account_object = Account(None, account_json_dictionary['balance'], account_json_dictionary['c_id'], account_json_dictionary['account_type'],
                               None)
    try:
        return account_service.add_account(account_object), 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


@ac.route('/customers/<c_id>/accounts/<account_id>', methods=['PUT'])
def edit_account_by_customer_id_and_account_id(c_id, account_id):
    pass


@ac.route('/customers/<c_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(c_id, account_id):
    pass