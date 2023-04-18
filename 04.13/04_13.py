from typing import List

class MyList:
    def __init__(self, items: List[int]) -> None:
        self.items = items


    def __bool__(self) -> bool:
        return False
    
    def __len__(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        return "Tiesiog kazkas"


my_list = MyList(items=[1,2,3])

print(bool(my_list))
print(len(my_list))
print(my_list)

print