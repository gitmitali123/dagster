from dagster import asset


@asset(required_resource_keys={"snowflake"})
def snowflake_table_asset(context, weather_data_asset):
    conn = context.resources.snowflake
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_table (temperature, humidity) VALUES (%s, %s)",
        (weather_data_asset["main"]["temp"], weather_data_asset["main"]["humidity"])
    )
    cursor.close()
    conn.close()