from typing import List

class Point:
    def __init__(self,x: float,y: float):
        self._x= x
        self._y= y

    def get_coordinates(self) -> List[float]:
        return [self._x,self._y, self.z]
    

    @property
    def z(self):
        return 2 * self._x
    

    @z.setter
    def z(self, value: float):
        self._x = value

    @z.deleter
    def z(self):
        del self._x 


my_point = Point(2.5, 6.3)
print(my_point.get_coordinates())
my_point.z = 20.5
print(my_point.get_coordinates())
