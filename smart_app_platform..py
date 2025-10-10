from weerstation import weerstation
from smart_app_controller import smart_app_controller
from weer_api import haal_huidig_weer_op

def smart_app():
    while True:
        print("\n--- Smart App Menu ---")
        print("1. Start Weerstation")
        print("2. Start Smart App Controller")
        print("3. Haal huidig weer op (API)")
        print("4. Stop")

        keuze = input("Kies een optie: ")

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app_controller()
        elif keuze == "3":
            haal_huidig_weer_op()
        elif keuze == "4":
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    smart_app()
