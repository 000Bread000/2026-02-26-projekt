# jatek.py
import random

def mentes_eredmeny(lepesek):
    with open("eredmenyek.txt", "a", encoding="utf-8") as f:
        f.write(f"Játékos nyert {lepesek} lépésből.\n")
    print("Eredmény elmentve!")

def jatek():
    gondolt_szam = random.randint(1, 100)
    lepesek = 0
    print("\nGondoltam egy számra 1 és 100 között. Találd ki!")
    
    while True:
        try:
            tipp = int(input("Tipped: "))
            lepesek += 1
            
            if tipp < gondolt_szam:
                print("Nagyobb számra gondoltam.")
            elif tipp > gondolt_szam:
                print("Kisebb számra gondoltam.")
            else:
                print(f"Gratulálok! Eltaláltad {lepesek} lépésből.")
                mentes_eredmeny(lepesek)
                break
        except ValueError:
            print("Kérlek, érvényes egész számot adj meg!") # Hibakezelés

while True:
    print("\n--- SZÁMKITALÁLÓS JÁTÉK ---")
    print("1. Új játék\n2. Kilépés")
    valasz = input("Válassz: ")
    
    if valasz == "1":
        jatek()
    elif valasz == "2":
        break
    else:
        print("Érvénytelen választás.")