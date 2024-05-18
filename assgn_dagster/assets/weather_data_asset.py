from dagster import asset
from ..resources.api_resource import fetch_weather_data

@asset(required_resource_keys={"api"})
def weather_data_asset(context):
    city = "New York"  # You can also make this configurable
    api_key = context.resources.api["api_key"]
    weather_data = fetch_weather_data(api_key, city)
    return weather_data