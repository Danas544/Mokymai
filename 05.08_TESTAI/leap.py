from typing import List

class Keliamieji:


    @staticmethod
    def tikrinti(metai: int) -> float:
        return (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)

    @staticmethod
    def diapazonas(nuo: int, iki: int) -> List[int]:
        sarasas = []
        for metai in range(nuo, iki):
            if (metai % 400 == 0) or (metai %100 != 0 and metai % 4 == 0):
                sarasas.append(metai)
        return sarasas
    


if __name__ == "__main__":
    print(Keliamieji.tikrinti(2020))