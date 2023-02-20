# Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis.
# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
from typing import Union
user = input("UserName: ")
password = input("Password: ")

def auth(user: str, password: str)-> Union[str,None]:
    real_user = "Danielius"
    real_pass = "Au74"
    if user == real_user and password == real_pass:
        try:
            linkas = home(Truee)
            return linkas +" Prisijungiai"
        except Exception as e:
            print(f"Klaida: {e}")
            linkas = home(True)
            return linkas + " Prisijungiai"
    else:
        try:
            linkas = home(Falsee)
            return linkas + " Blogi prisijungiai"
        except Exception as e:
            print(f"Klaida: {e}")
            linkas = home(True)
            return linkas + " Blogi prisijungiai"


def home(bool: bool)-> str:
    if bool == True:
        return "home.html"
    else:
        return "Login.html"
    
    
print(auth(user=user,password=password))