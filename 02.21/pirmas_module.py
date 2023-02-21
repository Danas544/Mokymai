from typing import Union

def calculate():
    Pasirinkimas = input('Pasirinkite funkcija: + <- sudečiai , - <- atimčiai , * <- daugybai , / <- dalybai : ')

    sk1 = input("Pirmas skačius: ")
    sk2 = input("Antras skačius: ")

    sk1p , sk2p = check_input(sk1 , sk2)
    if type(sk1p) == str:
        print(sk1p)
        kartojam()

    if Pasirinkimas == "+":
        rez = sk1p + sk2p
        print(rez)
        kartojam()
    elif Pasirinkimas == "-":
        rez = sk1p - sk2p
        print(rez)
        kartojam()
    elif Pasirinkimas == "*":
        rez = sk1p * sk2p
        print(rez)
        kartojam()
    elif Pasirinkimas == "/":
        try:
            rez = sk1p / sk2p
            print(rez)
            kartojam()
        except ZeroDivisionError:
            print("Dalyba iš nulio nesidalina")
            kartojam()
    else:
        print("Reikia butinai pasirinkti funkcija")
        kartojam()
    



def check_input(sk1: str , sk2: str) -> Union[tuple[int,int],tuple[float,float],tuple[str,str]]:
    try:
        sk11 = int(sk1)
        sk22 = int(sk2)
        return sk11 , sk22
    except ValueError:
        try:
            sk111 = float(sk1)
            sk222 = float(sk2)
            return sk111 , sk222
        except ValueError:
            return "Raides netinka seniuk :/" , ""


def kartojam() -> None:
    kart = input("Kartojam? y -> YES , n -> NO: ")
    if kart == "y":
        calculate()
    else:
        print("Viso gero")

def pasisveikinimas() -> None:
    print("Sveiki atvykę")


if __name__ =="__main__":
    print("valio")
    pasisveikinimas()
    calculate()
    kartojam()