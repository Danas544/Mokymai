


def add_lists(pirmas: list,antras:list) -> list[list]:


    pirmas.append(antras)
    return pirmas

if __name__=="__main__":
    print(add_lists([1,2],[3]))