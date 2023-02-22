import requests
import logging
import sys

def loginti(info):
    sys.getdefaultencoding()
    logging.basicConfig(level=logging.DEBUG, filename='./orai.log', filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    
    if info[:5] == "Kokie":
        logging.info(info)
    else:
        logging.error(info)





def orai(apikey: str, miestas: str) -> dict:
    try:
        oras = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{miestas}',
                            params={"unitGroup": "metric", "include": "days", "key": apikey , "contentType": "json"})

    except Exception as e:
        loginti(f"Blogai: {e}")
        return f"Blogai: {e}"
    if oras.status_code != 200:
        loginti(f"Blogai: {oras.status_code}")
        return f"Blogai: {oras.status_code}"
    print(oras.json())
    oras = oras.json()
    oru_listas = []
    pilni_orai = {}
    Vieta = oras["resolvedAddress"]
    pilni_orai["Vieta"] = Vieta
    laiko_zona = oras["timezone"]
    pilni_orai["laiko_zona"] = laiko_zona
    pilni_orai["Orai"] = oru_listas
    for duomenys in oras["days"]:
        # vienas["Orai"].append(duomenys["datetime"])
        try:
            data = duomenys["datetime"]
            temp = duomenys["temp"]
            jutimine = duomenys["feelslike"]
            komentaras = duomenys["description"]
            sauletekis = duomenys["sunrise"]
            saulelydis = duomenys["sunset"]
        except Exception as e:
            info = f"Blogai: {e}"
            loginti(info)
        # vienas["Orai"].append(duomenys["temp"])
        # vienas["Orai"] = vienas["Temperatura"] = duomenys["temp"]
        # vienas["Orai"].append(duomenys["feelslike"])

        vienas = {"Data": data,
                  "Temperatura": temp,
                  "Jutiminė temperatūra": jutimine,
                  "Komentaras": komentaras,
                  "Saulėtekis": sauletekis,
                  "Saulėlydis": saulelydis}
        oru_listas.append(vienas)
        #print(duomenys["datetime"])
        #print(duomenys["temp"])
        #print(duomenys["feelslike"])
    loginti(f"Kokie orai?: {pilni_orai}")
    return pilni_orai

if __name__ == "__main__":
    oras = orai("2MD9CK98TASDHLU9R3WDWH38Y", "Vilnius")
    #print(oras)