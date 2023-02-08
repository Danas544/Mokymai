order = {
    "id": 123,
    "price":{
      "amount":43.0,
      "currency":"EUR"
   },
    "Padalinys": {
        "id": 19191919191,
        "name": "Panorama"
    },
    "patiekalai": [
        {
           "type": "Patiekalas",
            "id": 881818181,
            "count": 1,
            "name": "Kebabas",
            "price": {
                "amount": 7.5,
                "currency": "EUR"
            },
             "modifikatoriai":[
                {
                   "id": 1919191981919,
                    "name": "MIKSAS",
                    "price": {
                        "amount": 10,
                        "currency": "EUR",
                    "count": 1   
                    } 
                }
             ]
        },
        {
          "type": "Patiekalas",
            "id": 191529828,
            "count": 1,
            "name": "Bulves free",
            "price": {
                "amount": 10.5,
                "currency": "EUR"
            },
             "modifikatoriai":[
                {
                   "id": 152941791298259,
                    "name": "Cesnakinis",
                    "price": {
                        "amount": 10,
                        "currency": "EUR",
                    "count": 1   
                    } 
                }
             ]  
        },
        {
           "type": "Patiekalas",
            "id": 1919198198195282,
            "count": 2,
            "name": "Cola",
            "price": {
                "amount": 2.5,
                "currency": "EUR"
            }
        }
    ]
}

#print(countries_and_capitals["Baltic"][0]["id"])

for x in order["patiekalai"]:
    a = x["id"]
    print(a)