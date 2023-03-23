# write a function that accepts an encoded string as a parameter. This string will contain a first name, last name,
# and an id.Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros.
# The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.An example
# input would be “Robert000Smith000123”. The function should return the following using that
# input:{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

from typing import Union
def encode_string_to_dict(text: str) -> str: # Jeigu gražinčiau tik dictory tada butu dict[str,Union[str,int]]

    clean_text = []
    for x in text.split("0"):
        if len(x) > 0:
            clean_text.append(x)

    dictory = {
        "first_name": clean_text[0],
        "last_name": clean_text[1],
        "id": clean_text[2],
    }
    return f"input:{dictory}"


print(encode_string_to_dict("Danielius00000000Aukstulevicius00000000001252752723"))
