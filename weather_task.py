import os
import requests
import random
import statistics

API_KEY = os.getenv("OWM_API_KEY")
if not API_KEY:
    raise SystemExit("Missing OWM_API_KEY. Set it before running (see README).")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"

# Списък с градове от целия свят
CITY_POOL = [
    "Sofia,BG", "Plovdiv,BG", "Varna,BG", "Burgas,BG",
    "London,GB", "Paris,FR", "Berlin,DE", "Rome,IT", "Madrid,ES",
    "New York,US", "Los Angeles,US", "Toronto,CA", "Vancouver,CA",
    "Tokyo,JP", "Seoul,KR", "Beijing,CN", "Sydney,AU", "Melbourne,AU",
    "Cairo,EG", "Istanbul,TR", "Athens,GR", "Stockholm,SE", "Oslo,NO",
    "Dubai,AE", "Singapore,SG", "Bangkok,TH", "Rio de Janeiro,BR", "Buenos Aires,AR"
]

def fetch_weather(city: str):
    """Връща JSON с времето за даден град или None при грешка."""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNITS}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None

def interpret_condition(weather_data):
    """Връща дали е слънчево, облачно или вали + емотикона."""
    weather_main = weather_data["weather"][0]["main"]
    clouds = weather_data.get("clouds", {}).get("all", 0)

    if weather_main in ["Rain", "Drizzle", "Thunderstorm"]:
        return "🌧️ вали"
    elif weather_main == "Snow":
        return "❄️ сняг"
    elif weather_main == "Clear":
        return "☀️ слънчево"
    elif clouds >= 50:
        return "☁️ облачно"
    else:
        return f"🌤️ {weather_data['weather'][0]['description']}"

def print_city_info(data):
    """Извежда информация за град."""
    name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = interpret_condition(data)
    print(f"- {name}: {condition}, 🌡️ {temp:.1f} °C, 💧 влажност {humidity}%")
    return name, temp

def five_random_cities():
    """Избира 5 случайни града и показва данните."""
    print("🌍 Времето в 5 случайни града:\n")
    chosen = random.sample(CITY_POOL, 5)
    temps = []
    for city in chosen:
        data = fetch_weather(city)
        if data:
            name, temp = print_city_info(data)
            temps.append((name, temp))
        else:
            print(f"- {city}: ❌ грешка при взимане на данни.")
    return temps

def show_statistics(temps):
    """Извежда статистики за градовете."""
    if not temps:
        print("\n❌ Няма данни за статистика.")
        return
    coldest_city, coldest_temp = min(temps, key=lambda x: x[1])
    avg_temp = statistics.mean(t for _, t in temps)
    print("\n📊 Статистики:")
    print(f"* 🥶 Най-студен град: {coldest_city} ({coldest_temp:.1f} °C)")
    print(f"* 🌡️ Средна температура: {avg_temp:.1f} °C")

def interactive_lookup():
    """Позволява на потребителя да въведе град и извежда инфо."""
    print("\n🔎 Проверка на град по избор (Enter за край):")
    while True:
        city = input("Въведи град (пример: London,GB): ").strip()
        if not city:
            break
        data = fetch_weather(city)
        if data:
            print_city_info(data)
        else:
            print("❌ Грешка: не може да се зареди информация.")

def main():
    temps = five_random_cities()
    show_statistics(temps)
    interactive_lookup()

if __name__ == "__main__":
    main()
