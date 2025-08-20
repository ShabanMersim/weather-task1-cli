# Task 1 — CLI Weather (OpenWeather)

Конзолно приложение, което:
- показва време за 5 случайни града (облачно/вали/слънчево, температура, влажност),
- извежда статистики (най-студен град, средна температура),
- позволява проверка на град по избор (напр. `London,GB`).

## Стартиране (Windows PowerShell)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

$env:OWM_API_KEY="YOUR_OPENWEATHER_KEY"
python .\weather_task.py

> Ако PowerShell блокира, в cmd.exe:
> .\.venv\Scripts\activate.bat
