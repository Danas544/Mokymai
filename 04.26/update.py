from model import Vaikas, Tevas
from session import session



# vaikas = Vaikas(vardas="Naujas vaikas", pavarde="Tevaika")
# tevas = session.query(Tevas).get(1)
# print(tevas)
# tevas.vaikas = vaikas
# print(tevas.vaikas)
# session.commit()


tevas = session.query(Tevas).get(1)
tevas.vaikas.pavarde = "Naujapavardaitis"
session.commit()