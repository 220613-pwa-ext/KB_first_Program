import psycopg

from model.user import User
from model.reimbs import Reimb

class UserDao:

    def get_user_by_username_password(self, username, password):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_users WHERE username = %s AND p_word = %s", (username, password))

                user_information = cur.fetchone()

                if user_information is None:
                    return None
                else:
                    u_id = user_information[0]
                    username = user_information[1]
                    password = user_information[2]
                    first_name = user_information[3]
                    last_name = user_information[4]
                    email = user_information[5]
                    gender = user_information[6]
                    phone_number = user_information[7]
                    role = user_information[8]

                    return User(u_id, username, password, first_name, last_name, gender, email, phone_number, role)

    def get_user_by_email(self, email):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_users WHERE e_mail = %s", (email,))

                user_information = cur.fetchone()

                if user_information is None:
                    return None

                username = user_information[0]
                password = user_information[1]
                first_name = user_information[2]
                last_name = user_information[3]
                gender = user_information[4]
                email = user_information[5]
                phone_number = user_information[6]
                role = user_information[7]

                return User(None, username, password, first_name, last_name, gender, email, phone_number, role)

    def get_user_by_username(self,username):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonem102123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_users WHERE username = %s", (username,))

                user_information = cur.fetchone()

                if user_information is None:
                    return None

                username = user_information[0]
                password = user_information[1]
                first_name = user_information[2]
                last_name = user_information[3]
                gender = user_information[4]
                email = user_information[5]
                phone_number = user_information[6]
                role = user_information[7]

                return User(None, username, password, first_name, last_name, gender, email, phone_number, role)

    def add_user(self, user_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO ers_users VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (user_obj.username, user_obj.password, user_obj.first_name, user_obj.last_name, user_obj.gender,
                                                                                       user_obj.email, user_obj.phone_number, user_obj.role))

                user_inserted = cur.fetchone()
                if user_inserted is None:
                    return None
                else:
                    return User(None, user_inserted[0], user_inserted[1], user_inserted[2], user_inserted[3], user_inserted[4], user_inserted[5], user_inserted[6], user_inserted[7])

    def get_reimb_by_employee_id(self, u_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursement WHERE reimb_author = (%s)", (u_id,))

                reimbs_list = []
                user_information = cur.fetchall()
                if user_information is None:
                    return None
                else:
                    for row in user_information:
                        reimbs_list.append(Reimb(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                    return reimbs_list

    def get_reimb_by_manager_id(self, u_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursement WHERE reimb_resolver= %s", (u_id,))

                reimbs_list = []
                user_information = cur.fetchall()
                if user_information is None:
                    return None
                else:
                    for row in user_information:
                        reimbs_list.append(Reimb(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                    return reimbs_list

    def update_reimb_by_id(self, reimb_id, stat):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="Hateonme102123") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE ers_reimbursement SET status = %s WHERE reimb_id = %s RETURNING *", (stat, reimb_id))

                update_reimb_stat = cur.fetchone()
                if update_reimb_stat is None:
                    return None
                else:
                    conn.commit()
                    return Reimb(update_reimb_stat[0],update_reimb_stat[1], update_reimb_stat[2], update_reimb_stat[3], update_reimb_stat[4], update_reimb_stat[5], update_reimb_stat[6],
                                 update_reimb_stat[7], update_reimb_stat[8], update_reimb_stat[9])