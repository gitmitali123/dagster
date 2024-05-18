from dagster import job
from ..assets.weather_data_asset import weather_data_asset
from ..assets.snowflake_table_asset import snowflake_table_asset

@job
def weather_job():
    snowflake_table_asset(weather_data_asset())