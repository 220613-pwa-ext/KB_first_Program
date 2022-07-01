class Customer:
    def __init__(self, c_id, c_name, last_name, p_word,e_mail,gender):
        self.c_id = c_id
        self.c_name = c_name
        self.last_name = last_name
        self.p_word = p_word
        self.e_mail = e_mail
        self.gender = gender

    def to_dict(self):
        return {
            "c_id": self.c_id,
            "c_name": self.c_name,
            "last_name": self.last_name,
            "p_word": self.p_word,
            "e_mail": self.e_mail,
            "gender": self.gender
        }
