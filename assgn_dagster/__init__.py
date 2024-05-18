from dagster import Definitions, load_assets_from_modules, with_resources
from .assets import weather_data_asset, snowflake_table_asset
from .resources.api_resource import api_resource
from .resources.snowflake_resource import snowflake_resource
from .jobs.weather_job import weather_job
all_assets = load_assets_from_modules([weather_data_asset, snowflake_table_asset])

defs = Definitions(
    assets=with_resources(all_assets, resource_defs={
        "api": api_resource,
        "snowflake": snowflake_resource
    }),
   # jobs=[weather_job]
)
