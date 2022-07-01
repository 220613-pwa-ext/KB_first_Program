import psycopg
from model.account import Account


class AccountDao:

    def get_all_account_by_customer_id(self, c_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE c_id = %s", (c_id,))

                account_list = []

                for row in cur:
                    account_list.append(Account(row[0], row[1], row[2], row[3], row[4]))

                return account_list

    def add_account(self, account_object):
        balance_to_add = account_object.balance
        c_id_to_add = account_object.c_id
        account_type_to_add = account_object.account_type

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (balance, c_id,account_type) SELECT %s, customers.id,%s FROM customers WHERE customers.id=%s RETURNING *", (balance_to_add,
                                                                                                                                                                account_type_to_add,c_id_to_add))

                customer_row_that_was_just_inserted = cur.fetchone()

                conn.commit()

                return Account(None, customer_row_that_was_just_inserted[0], customer_row_that_was_just_inserted[1],
                            customer_row_that_was_just_inserted[2], None)
