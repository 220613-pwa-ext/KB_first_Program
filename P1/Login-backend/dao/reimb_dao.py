import psycopg
from model.reimbs import Reimb


class ReimbDao:

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