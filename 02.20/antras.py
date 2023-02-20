# Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.
#  Sukurkite funkciją, kuri apimtų visą klaidų tvarkymo ciklą (try/except/else/finally) su realaus pasaulio scenarijaus pavyzdžiu.

dictor = {"A": 1,
          "B": 2}

def fu(dictor) -> None:
    try:
        print(dictor["A"])
    except KeyError as e:
        print(f"Error: Nėra tokio key {e}")
    else:
        print("viskas oK")
    finally:
        for a in dictor.items():
            print(a)

fu(dictor)