from Practice_11 import Database

class UserService:
    def __init__ (self, db):
        self.db = db

    def register_user(self, user_id, name):
        self.db.add_user(user_id, name)

    def fetch_user(self, user_id):
        return self.db.get_user(self, user_id)
    
