import bcrypt
from ..models import Database

class AuthController:
    def __init__(self):
        self.db = Database()

    def verify_credentials(self, username, password):
        user = self.db.get_user_by_username(username)
        if user:
            stored_password = user['password_hash']
            return bcrypt.checkpw(password.encode('utf-8'), stored_password)
        return False
