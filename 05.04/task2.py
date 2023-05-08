# Task Nr.2 :
# Write a User class that has a password property.
#  The password property should be a computed property that checks whether the password is strong enough.
#  A password is considered strong if it has at least 8 characters, contains at least one uppercase letter, one lowercase letter, and one number.
# Parašykite vartotojo klasę, kuri turi slaptažodžio ypatybę.
# Slaptažodžio ypatybė turėtų būti apskaičiuota, tikrinanti, ar slaptažodis pakankamai stiprus.
# Slaptažodis laikomas stipriu, jei jame yra bent 8 simboliai, bent viena didžioji raidė, viena mažoji raidė ir vienas skaičius.

import re


class User:
    def __init__(self):
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        if self.is_strong_password(password) is False:
            raise ValueError("Not strong password")
        self._password = password

    @staticmethod
    def is_strong_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        return True


user = User()
user.password = "Danielius54"
print(user.password)
