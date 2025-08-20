# Task 1 — CLI Weather (OpenWeather)

Task 1. Weather API requests - основи
Да се напише програма, която:

Да показва какво е времето в момента за 5 произволно избрани града (бонус точки: град от цял свят, няма ограничение - освен да е написан на латиница):

Дали е облачно/вали или е слънчево ?
Каква е температурата в момента ?
Каква е влажността в момента ?
Да се изведе следните статистики:

Най-студен град (от избраните 5)
Средна температура (от избраните 5)
Да може да се въвежда име на град и индивидуално да изкарва статистика: (бонус точки)

Облачно ли е ?
Каква е температурата ?
Каква е влажността в момента ?
Нужни неща:

Обработване на JSON данни
HTTP/HTTPS Requests
Random generator
User Input
http://openweathermap.org/api

## Стартиране (Windows PowerShell)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

$env:OWM_API_KEY="YOUR_OPENWEATHER_KEY"
python .\weather_task.py

> Ако PowerShell блокира, в cmd.exe:
> .\.venv\Scripts\activate.bat
