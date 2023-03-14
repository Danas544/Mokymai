# Create a Plane, Boeing, Airbus classes.
# Base class should contain methods to get:  plane name, plane type (A320, B737 etc), max_speed (should be the funciotn: base_speed * model_speed_coeficient).
# Both plane subclasses should only take model type as input argument.

class Plane:
    BASE_SPEED = 750
    def __init__(self, model_type:str, mode_speed_coeficient: float , name_sufix) -> None:
        self.model_type = model_type
        self.mode_speed_coeficient = mode_speed_coeficient
        self.name_sufix = name_sufix
    
    def get_plane_name(self)->str:
        return self.name_sufix + self.model_type
    
    def get_plane_type(self) -> str:
        return self.model_type
    
    def get_max_speed(self) -> str:
        return self.BASE_SPEED * self.mode_speed_coeficient
        



class Boeing(Plane):
    NAME_SUFIX = 'B'

    BOEING_TYPE_SPEED_COEF = {
        "737": 1,
        "747": 1.2,
        "757": 1.35,
        "767": 1.5,
        "777": 1.8,
                }

    def __init__(self , model:str) -> None:
        self.model = model
        speed_coef = self._get_type_speed_coef()
        super().__init__(name_sufix= self.NAME_SUFIX, model_type= model , mode_speed_coeficient= speed_coef)

    def _get_type_speed_coef(self)-> float:
        return self.BOEING_TYPE_SPEED_COEF.get(self.model)



class Airbus(Plane):
    NAME_SUFIX = 'A'
    def __init__(self, model:str ,) -> None:
        super().__init__(plane_name=self.NAME_SUFIX, model_type=model)



my_plane = Boeing("777")
print(my_plane.get_plane_name())
print(f"KM/H {my_plane.get_max_speed()}")
