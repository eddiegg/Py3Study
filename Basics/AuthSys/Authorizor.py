from AuthSys.AuthException import InvalidUsername, NotLoggedInError, NotPermittedError
from AuthSys.Authenticator import authenticator


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:        #不存在就加入
            self.permissions[perm_name] = set()
        else:                   #存在就报错
            raise PermissionError("Permission Exists")

    def permit_user(self,perm_name,username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self,perm_name,username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

authorizor = Authorizor(authenticator)