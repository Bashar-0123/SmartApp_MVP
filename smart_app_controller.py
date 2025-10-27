def lees_invoerbestand():
    try:
        with open("input_bestanden/input.txt", "r") as bestand:
            regels = bestand.readlines()
        return regels
    except FileNotFoundError:
        print("Bestand niet gevonden. Controleer of input.txt bestaat.")
        return []


def schrijf_output(data):
    with open("output_actuatoren.txt", "w") as bestand:
        for regel in data:
            bestand.write(regel + "\n")


def smart_app_controller():
    print("=== Smart App Controller ===")
    regels = lees_invoerbestand()
    if not regels:
        print("Geen data beschikbaar in input.txt")
        return

    resultaten = []

    for index, regel in enumerate(regels, start=1):
        delen = regel.strip().split(",")
        if len(delen) != 3:
            continue

        try:
            temp = float(delen[0])
            vocht = int(delen[1])
            wind = float(delen[2])
        except:
            print(f"Ongeldige data in regel {index}, overgeslagen.")
            continue

        if temp < 15:
            cv = 50
        else:
            cv = 0

        if vocht < 30:
            ventilatie = 4
        elif vocht > 70:
            ventilatie = 2
        else:
            ventilatie = 3

        bewatering = vocht < 40

        datum = f"{index:02d}-10-2025"

        regel_output = f"{datum};{cv};{ventilatie};{bewatering}"
        resultaten.append(regel_output)
        print(regel_output)

    schrijf_output(resultaten)
    print("Resultaten opgeslagen in output_actuatoren.txt")
