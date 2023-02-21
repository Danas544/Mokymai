from typing import Union


def add(sk1:Union[float,int], sk2:Union[float,int]) -> Union[float,int,str]:

    if type(sk1) and type(sk2) == int == int:
        rez = sk1 + sk2
        return rez
    elif type(sk1) and type(sk2) == float == float:
        rez = sk1 + sk2
        return rez
    elif type(sk1) and type(sk2) == int == float:
        rez = sk1 + sk2
        return rez
    elif type(sk1) and type(sk2) == float == int:
        rez = sk1 + sk2
        return rez

    return "Tik skaiciai"
