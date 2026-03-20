# todo.py
import json
import os

FAJLNEV = "feladatok.json"
1
def betoltes():
    if os.path.exists(FAJLNEV):
        with open(FAJLNEV, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def mentes(adatok):
    with open(FAJLNEV, "w", encoding="utf-8") as f:
        json.dump(adatok, f, indent=4, ensure_ascii=False)

feladatok = betoltes()

while True:
    print("\n--- TO-DO LISTA ---")
    for i, f in enumerate(feladatok):
        print(f"{i+1}. {f['nev']} - Határidő: {f['hatarido']} - Státusz: {f['statusz']}")
    
    print("\n1. Új feladat\n2. Feladat törlése\n3. Státusz módosítása\n4. Kilépés")
    valasz = input("Válassz egy opciót: ")
    
    if valasz == "1":
        nev = input("Feladat neve: ")
        if not nev.strip():
            print("Nem lett megadva feladat név.")
            continue
        hatarido = input("Határidő (pl. 2026-03-05): ")
        if not hatarido:
            print("Nem lett megadva érvényes határidő!")
            continue
        feladatok.append({"nev": nev, "hatarido": hatarido, "statusz": "folyamatban"})
        mentes(feladatok)
        print("Feladat hozzáadva és elmentve!")
    
    elif valasz == "2":
        try:
            sorszam = int(input("Törlendő feladat sorszáma: ")) - 1
            if 0 <= sorszam < len(feladatok):
                torolt = feladatok.pop(sorszam)
                mentes(feladatok)
                print(f"'{torolt['nev']}' törölve!")
            else: print("Nincs ilyen sorszám.")
        except ValueError: print("Számot adj meg!")
        
    elif valasz == "3":
        try:
            sorszam = int(input("Módosítandó feladat sorszáma: ")) - 1
            if 0 <= sorszam < len(feladatok):
                feladatok[sorszam]["statusz"] = "kész"
                mentes(feladatok)
                print("Státusz 'kész'-re állítva!")
            else: print("Nincs ilyen sorszám.")
        except ValueError: print("Számot adj meg!")
        
    elif valasz == "4":
        break