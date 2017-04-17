import AuthSys

AuthSys.Authenticator.authenticator.add_user("eddie", "eddiepwd")
AuthSys.Authorizor.authorizor.add_permission("test program")
AuthSys.Authorizor.authorizor.add_permission("change program")
AuthSys.Authorizor.authorizor.permit_user("test program", "eddie")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = AuthSys.Authenticator.authenticator.login(
                    username, password)
            except AuthSys.AuthException.InvalidUsername:
                print("Sorry, that username does not exist")
            except AuthSys.AuthException.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            AuthSys.Authorizor.authorizor.check_permission(permission, self.username)
        except AuthSys.AuthException.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except AuthSys.AuthException.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True


    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")


    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")


    def quit(self):
        raise SystemExit()


    def menu(self):
        try:
            answer = ""
            while True:
                print("""
            Please enter a command:
            \tlogin\tLogin
            \ttest\tTest the program
            \tchange\tChange the program
            \tquit\tQuit
            """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")

Editor().menu()

