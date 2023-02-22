# Create a module and import any PIP package of your choice. Then create a function that would use it. Import that function to the main.py module and use it.
# Sukurkite modulį ir importuokite bet kurį pasirinktą PIP paketą. Tada sukurkite funkciją, kuri jį naudotų. Importuokite tą funkciją į main.py modulį ir ją naudokite.
from trecias_modulis import orai
import json


oras = orai("2MD9CK98TASDHLU9R3WDWH38Y", "Vilnius")
jsonas = json.dumps(oras, indent=2 ,ensure_ascii=False)
print(jsonas)