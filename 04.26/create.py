from model import Vaikas, Tevas
from session import session

# vaikas = Vaikas(vardas="vaiko_vardas2",pavarde= 'vaiko_pavarde2', mokymo_istaiga= 'vaiko_mokymo_istaiga2')





tevas = Tevas(vardas="Tevas_vardas2",pavarde= 'Tevas_pavarde2')


session.add(tevas)
session.commit()