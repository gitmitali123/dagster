from dagster import resource
from snowflake import connector

@resource(config_schema={"user": str, "password": str, "account": str, "database": str, "schema": str})
def snowflake_resource(context):
    conn = connector.connect(
        user=context.resource_config["user"],
        password=context.resource_config["password"],
        account=context.resource_config["account"],
        database=context.resource_config["database"],
        schema=context.resource_config["schema"]
    )
    return conn