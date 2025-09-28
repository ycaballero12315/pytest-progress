class Database:
    def __init__(self):
        self.data = {} #simulating an in memory database
    
    def add_user_id(self, user_id, name):
        if user_id in self.data:
            raise ValueError('User already exists')
        self.data[user_id] = name
    
    def get_user_id(self, user_id):
        return self.data.get(user_id, None)
    
    def delete_user_id(self, user_id):
        if user_id in self.data:
            del self.data[user_id]