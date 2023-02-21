from typing import Union

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
            return sk1, sk2
