import datetime

pradzia = datetime.datetime.today()
for x in range(1000000):
    print(x)

pabaiga = datetime.datetime.today()
print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")