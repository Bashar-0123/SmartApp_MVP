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
            verwarming = "Verwarming aan"
        elif temp > 25:
            verwarming = "Airco aan"
        else:
            verwarming = "Niets nodig"

        if vocht < 30:
            bewatering = "Bewatering aan"
        elif vocht > 70:
            bewatering = "Bewatering uit"
        else:
            bewatering = "Bewatering niets"

        if wind < 40:
            lampen = "Lampen aan"
        else:
            lampen = "Lampen uit"

        actie = f"{verwarming}, {bewatering}, {lampen}"
        resultaten.append(actie)
        print(f"Dag {index}: {actie}")

    schrijf_output(resultaten)
    print("\nResultaten opgeslagen in output_actuatoren.txt")
