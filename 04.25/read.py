from session import session
from main import Projektas,table2,table3,table5


# search2 = session.query(Projektas).filter(Projektas.price > 1000)
# list_price = []
#
# for i in search2:
#     list_price.append(i.price)
#
#
# print(sum(list_price))


project1 = session.query(Projektas).get(1)
print(project1.price)
project1.price = 100
session.add_all(project1)