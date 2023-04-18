# r = requests.get('https://www.b.eviteja.lt/')
# if r.ok:
#     print('važiuojam toliau!')
#     print(r.headers)
# else:
#     print(f'Klaida! kodas {r.status_code}')

# {
#   "colors": [
#     {
#       "color": "black",
#       "rgb": "255, 255, 255",
#       "hex": "#000"
#     },
#     {
#       "color": "white",
#       "rgb": "0, 0, 0",
#       "hex": "#FFF"
#     }



from typing import Union, List, Dict, Hex
import json
import requests


def get_data_dict(
    request: str
) -> Union[Dict[str, List[Dict[str, Union[str, Dict[str, Union[list[int], str]]]]]], str]:
    data = requests.get(request , timeout=10)
    if not data.ok:
        return f"Klaida! kodas: {data.status_code}"
    return json.loads(data.content)


data = get_data_dict(
    "https://raw.githubusercontent.com/robotautas/kursas/master/requests/uzduotis.json"
)
print(data)

if type(data) is not dict:
    print(data)
    exit()



for x in data["colors"]:
    del x["category"]
    try:
        del x["type"]
    except KeyError:
        pass
    x["rgb"] = ", ".join([str(y) for y in x["code"]["rgba"]])
    x["hex"] = x["code"]["hex"]
    del x["code"]


with open("new_uzduotis.json", "w") as file:
    json.dump(data, file, indent=2)
