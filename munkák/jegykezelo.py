# jegykezelo.py
diakok = {
    "Kovacs Janos": {"Matek": [4, 5], "Magyar": [3, 4]},
    "Nagy Anna": {"Matek": [5, 5], "Magyar": [4, 5]}
}

def atlag_szamitas(jegyek):
    if not jegyek: return 0
    return sum(jegyek) / len(jegyek)

def tanar_menu():
    while True:
        print("\n--- TANÁRI MENÜ ---")
        print("1. Diákok és jegyek listázása\n2. Új jegy rögzítése\n3. Kilépés")
        valasz = input("Válassz: ")
        
        if valasz == "1":
            for diak, targyak in diakok.items():
                print(f"\n{diak}:")
                for targy, jegyek in targyak.items():
                    print(f"  {targy}: {jegyek} (Átlag: {atlag_szamitas(jegyek):.2f})")
        elif valasz == "2":
            nev = input("Diák neve: ")
            if nev not in diakok:
                diakok[nev] = {}
                print("Új diák hozzáadva!")
            targy = input("Tantárgy: ")
            if targy not in diakok[nev]:
                diakok[nev][targy] = []
            try:
                jegy = int(input("Jegy (1-5): "))
                if 1 <= jegy <= 5:
                    diakok[nev][targy].append(jegy)
                    print("Jegy sikeresen rögzítve!")
                else: print("Érvénytelen jegy!")
            except ValueError:
                print("Kérlek, számot adj meg!")
        elif valasz == "3":
            break

def diak_menu():
    nev = input("Add meg a neved a belépéshez: ")
    if nev in diakok:
        print(f"\n--- {nev} JEGYEI ---")
        for targy, jegyek in diakok[nev].items():
            print(f"  {targy}: {jegyek} (Átlag: {atlag_szamitas(jegyek):.2f})")
    else:
        print("Nem található ilyen diák a rendszerben.")

# Főprogram
print("Üdvözöl a Jegykezelő Rendszer!")
szerepkor = input("Belépés mint (tanar / diak): ").strip().lower()
if szerepkor == "tanar":
    tanar_menu()
elif szerepkor == "diak":
    diak_menu()
else:
    print("Ismeretlen jogosultság.")