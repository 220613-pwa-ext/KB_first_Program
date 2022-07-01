from model.customer import Customer
import psycopg


class CustomerDao:


    def get_all_customers(self):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                my_list_of_customer_objs = []

                for customer in cur:
                    c_id = customer[0]
                    c_name = customer[1]
                    last_name = customer[2]
                    p_word = customer[3]
                    e_mail = customer[4]
                    gender = customer[5]

                    my_customer_obj = Customer(c_id, c_name, last_name, p_word, e_mail, gender)
                    my_list_of_customer_objs.append(my_customer_obj)

                return my_list_of_customer_objs


    def delete_customer_by_id(self, c_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers WHERE id = %s", (c_id,))


                row_deleted = cur.rowcount

                if row_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True


    def add_customer(self, customer_object):
        c_name_to_add = customer_object.c_name
        last_name_to_add = customer_object.last_name
        p_word_to_add = customer_object.p_word
        e_mail_to_add = customer_object.e_mail
        gender_to_add = customer_object.gender

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (c_name, last_name,p_word,e_mail,gender) VALUES (%s, %s,%s, %s,%s) RETURNING *", (c_name_to_add,
                                                                                                       last_name_to_add, p_word_to_add, e_mail_to_add, gender_to_add))

                customer_row_that_was_just_inserted = cur.fetchone()

                conn.commit()

                return Customer(customer_row_that_was_just_inserted[0], customer_row_that_was_just_inserted[1],
                            customer_row_that_was_just_inserted[2], customer_row_that_was_just_inserted[3], customer_row_that_was_just_inserted[4],customer_row_that_was_just_inserted[5])

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:

                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                c_id = customer_row[0]
                c_name = customer_row[1]
                last_name = customer_row[2]
                p_word = customer_row[3]
                e_mail = customer_row[4]
                gender = customer_row[5]

                return Customer(c_id, c_name, last_name, p_word, e_mail, gender)


    def update_customer_by_id(self, customer_object):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password=) as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET c_name = %s, last_name = %s, p_word = %s, e_mail = %s, gender = %s WHERE id = %s RETURNING *",
                            (customer_object.c_name, customer_object.last_name, customer_object.p_word, customer_object.e_mail, customer_object.gender, customer_object.c_id))

                conn.commit()

                update_customer_row = cur.fetchone()
                if update_customer_row is None:
                    return None

                return Customer(update_customer_row[0], update_customer_row[1], update_customer_row[2], update_customer_row[3], update_customer_row[4], update_customer_row[5])
