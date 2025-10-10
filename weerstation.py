import os

def naar_fahrenheit(temp_c):
    return 32 + 1.8 * temp_c

def gevoel_temp(temp, wind, vocht):
    return temp - (vocht / 100) * wind

def rapport(temp, wind, vocht):
    gevoel = gevoel_temp(temp, wind, vocht)
    if gevoel < 0 and wind > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and wind <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel >= 0 and gevoel < 10 and wind > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel >= 0 and gevoel < 10 and wind <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation():
    print("=== Weerstation (max 7 dagen). Laat temperatuur leeg om te stoppen. ===")
    temperaturen = []
    regels = []
    os.makedirs("input_bestanden", exist_ok=True)

    for dag in range(1, 8):
        t = input(f"Dag {dag} - temperatuur (C): ")
        if t.strip() == "":
            print("Stop ingevoerd. Programma stopt.")
            break
        try:
            t = float(t)
        except:
            print("Ongeldige waarde, probeer opnieuw.")
            continue

        w = input(f"Dag {dag} - windsnelheid (m/s): ")
        try:
            w = float(w)
        except:
            print("Ongeldige waarde, probeer opnieuw.")
            continue

        v = input(f"Dag {dag} - vochtigheid (%): ")
        try:
            v = int(v)
            if v < 0 or v > 100:
                print("Vochtigheid moet tussen 0 en 100 zijn.")
                continue
        except:
            print("Ongeldige waarde.")
            continue

        temperaturen.append(t)
        regels.append(f"{t},{v},{w}")
        f = naar_fahrenheit(t)
        r = rapport(t, w, v)
        gem = sum(temperaturen) / len(temperaturen)
        print(f"Het is {t:.1f}C ({f:.1f}F)")
        print(r)
        print(f"Gem. temperatuur tot nu toe: {gem:.1f}")
        print("-" * 30)

    with open("input_bestanden/input.txt", "w") as bestand:
        for regel in regels:
            bestand.write(regel + "\n")
    print("Data opgeslagen in input_bestanden/input.txt")
