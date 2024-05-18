import requests
from dagster import resource

@resource(config_schema={"api_key": str})
def api_resource(context):
    return {
        "api_key": context.resource_config["api_key"]
    }

def fetch_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()