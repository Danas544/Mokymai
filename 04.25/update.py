from session import session
from main import Projektas,table2,table3,table5



project1 = session.query(Projektas).get(1)
print(project1.price)
project1.price = 100
session.add_all(project1)