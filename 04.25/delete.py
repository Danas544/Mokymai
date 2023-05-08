
from session import session
from main import Projektas,table2,table3,table5

projektas1 = session.query(Projektas).filter_by(name="Naujas pr.").first()
print(projektas1)
session.delete(projektas1)
session.commit()