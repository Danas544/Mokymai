def add(x: int,y: int) -> int:
     return x + y
 

def sub(x: int,y: int) -> int:
     return x - y
 

def prod(x: int,y: int) -> int:
    return x * y
 

def div(x: int,y: int) -> int:
    return x // y


def add_sub_last(x: int , y: int, c: int = 10) -> int:
     return x + y - c


if __name__=="__main__":
    
    a = 10
    b = 20
    print("calc")
    print(add(a,b))