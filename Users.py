class User:
    def __init__(self, ID, naim):
        self._protected_ID = ID  # защищенный атрибут
        self._protected_naim = naim  # защищенный атрибут
        self._protected_access = 'user'  # защищенный атрибут
    def get_naim(self):
        return self._protected_naim
    def set_naim(self, naim):
        self._protected_naim = naim

class Admin(User):
    def __init__(self, ID, naim):
        super().__init__(ID, naim)
        self._protected_users = []
        user0 = User(ID, naim)
        user0._protected_access = 'admin'
        self._protected_users.append(user0)
    def add_user(self, ID, naim):
        user = User(ID, naim)
        self._protected_users.append(user)
    def remove_user(self, ID):
        for user in self._protected_users:
            if user._protected_ID == ID:
                self._protected_users.remove(user)
                break
    def set_rename(self, ID, naim):
        for user in self._protected_users:
            if user._protected_ID == ID:
                user.set_naim(naim)
                break
    #def view(self):
     #   return "\n".join(str(user._protected_naim) for user in self._protected_users)
    def view(self):
        return [[user._protected_access, user._protected_naim] for user in self._protected_users]
    def get_users(self):
        return self._protected_users

UserManager = Admin(0, 'Elena')
UserManager.add_user(1, 'Ivan')
UserManager.add_user(2, 'Dima')
UserManager.remove_user(1)
UserManager.set_rename(0,'Alex')
print(UserManager.view())

users = UserManager.get_users()
print(users[0].get_naim())