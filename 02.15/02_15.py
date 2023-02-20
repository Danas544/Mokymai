pirmas = [1, 2, 3, 4]
antras = [4, 3, 2, 1]
def puzzle(pirmas_listas: list , antras_listas: list)-> bool:
    bendras = []
    for pirm, antr in zip(pirmas, antras):
        sudetis = pirm + antr
        bendras.append(sudetis)
    tikrinam = bendras[0]
    for x in bendras:
        if x == tikrinam:
            pass
        else:
            return False
    return True



print(puzzle(pirmas,antras))

