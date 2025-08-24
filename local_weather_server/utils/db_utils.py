from __future__ import annotations

import sqlite3

from local_weather_server.models.database import WeatherData
from local_weather_server.models.database import WeatherStation


def insert_weather_station(
        db: sqlite3.Connection,
        weather_station: WeatherStation,
) -> None:
    station = db.execute(
        'SELECT id FROM weather_station WHERE id = ?',
        (weather_station.id,),
    ).fetchone()

    if not station:
        values = (
            weather_station.id,
            (
                str(weather_station.timezone)
                if weather_station.timezone else None
            ),

        )
        db.execute(
            'INSERT INTO weather_station (id, timezone) VALUES (?, ?)',
            values,
        )


def insert_weather_data(
        db: sqlite3.Connection,
        weather_data: WeatherData,
) -> None:
    insert_weather_station(db=db, weather_station=weather_data.weather_station)
    values = (
        int(weather_data.timestamp.timestamp()),
        weather_data.weather_station.id,
        weather_data.temperature,
        weather_data.humidity,
        weather_data.dew_point,
        weather_data.feels_like,
        weather_data.absolute_pressure,
        weather_data.relative_pressure,
        weather_data.rainfall_rate,
        weather_data.daily_rain,
        weather_data.weekly_rain,
        weather_data.monthly_rain,
        weather_data.yearly_rain,
        weather_data.wind_speed,
        weather_data.wind_gust_speed,
        weather_data.wind_direction,
        weather_data.solar_radiation,
        weather_data.uv_index,
    )
    db.execute(
        'INSERT INTO weather_data (timestamp, weather_station_id, '
        'temperature, humidity, dew_point, feels_like, '
        'absolute_pressure, relative_pressure, rainfall_rate, '
        'daily_rain, weekly_rain, monthly_rain, yearly_rain, wind_speed, '
        'wind_gust_speed, wind_direction, solar_radiation, '
        'uv_index) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        values,
    )
