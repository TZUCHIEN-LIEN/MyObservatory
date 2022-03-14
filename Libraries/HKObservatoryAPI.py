import requests
import json
import datetime

QUERY_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
QUERY_DATA = {"dataType": "fnd", "lang": "en"}


def query_weather():
    r = requests.get(QUERY_URL, QUERY_DATA)
    if r.status_code != 200:
        raise RuntimeError(f"Failed to query weather! Status code is {r.status_code}, reason is {r.reason}")

    formated_report = json.loads(r.content)
    weather_forecast = formated_report["weatherForecast"]
    return weather_forecast


def get_2_day_later_humidity():
    two_day_later = datetime.date.today() + datetime.timedelta(days=2)
    dateformatter = "%Y%m%d"
    two_day_later = two_day_later.strftime(dateformatter)

    weather_forecast = query_weather()
    for element in weather_forecast:
        if element.get("forecastDate") == two_day_later:
            low_humidity = element.get("forecastMinrh").get("value")
            high_humidity = element.get("forecastMaxrh").get("value")
        else:
            continue
    return f"{low_humidity}-{high_humidity}%"


if __name__ == "__main__":
    get_2_day_later_humidity()