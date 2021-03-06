from werkzeug.security import check_password_hash
import bcrypt


class User():

    def __init__(self, username):
        self.username = username

    def hash_pass(password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
        
    #@staticmethod
    def validate_login(password_hash, password):
        return bcrypt.hashpw(bytes(password, 'utf-8'), password_hash) == password_hash