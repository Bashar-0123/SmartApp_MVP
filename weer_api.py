import requests

def haal_huidig_weer_op():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.37&longitude=4.90&current_weather=true"
        reactie = requests.get(url)
        data = reactie.json()

        if "current_weather" in data:
            weer = data["current_weather"]
            temp = weer["temperature"]
            wind = weer["windspeed"]
            print(f"\n🌤️ Huidig weer in Amsterdam:")
            print(f"Temperatuur: {temp}°C")
            print(f"Windsnelheid: {wind} km/u\n")
        else:
            print("Geen actuele weerdata gevonden.")
    except Exception as e:
        print(f"Fout bij het ophalen van weerdata: {e}")
