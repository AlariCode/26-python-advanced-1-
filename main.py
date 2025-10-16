"""Демо модуль для курса"""


class Auth:
    is_authed: bool = False

    def login(self):
        self.is_authed = True

    def logout(self):
        """Выход"""
        self.is_authed = False


auth_service = Auth()
auth_service.login()
auth_service.logout()
# Auth.login(auth_service)
print(auth_service.is_authed)
