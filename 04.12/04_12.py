import csv
import datetime
from bs4 import BeautifulSoup
import requests
import os

if not os.path.exists("Telia telefonai.csv"):
    with open("Telia telefonai.csv", "w", encoding="UTF-8", newline="") as failas:
        csv_writer = csv.writer(failas)
        csv_writer.writerow(["Modelis", "Mėnesio kaina", "Kaina"])

puslapis = 0
while True:
    source = requests.get(
        f"https://www.telia.lt/prekes/mobilieji-telefonai?q=%3Arelevance&page={puslapis}"
    ).text

    soup = BeautifulSoup(source, "html.parser")

    blokai = soup.find_all(
        "div",
        class_="mobiles-product-card card card__product card--anim js-product-compare-product",
    )
    if blokai != []:
        puslapis += 1
        with open("Telia telefonai.csv", "a", encoding="UTF-8", newline="") as failas:
            csv_writer = csv.writer(failas)
            for blokas in blokai:
                pavadinimas = blokas.find(
                    "a", class_="mobiles-product-card__title js-open-product"
                ).text.strip()
                men_kaina = blokas.find(
                    "div", class_="mobiles-product-card__price-marker"
                ).text.strip()
                kaina = blokas.find_all("div", class_="mobiles-product-card__price-marker")[
                    1
                ].text.strip()
                print(pavadinimas, men_kaina, kaina)
                csv_writer.writerow([pavadinimas, men_kaina, kaina])
    else:
        break


os.rename(f"Telia telefonai.csv", f'Telia telefonai {datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.csv')
