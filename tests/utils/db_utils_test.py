from __future__ import annotations

import datetime
import zoneinfo

from local_weather_server.models.database import WeatherData
from local_weather_server.models.database import WeatherStation
from local_weather_server.utils.db_utils import insert_weather_data
from local_weather_server.utils.db_utils import insert_weather_station


def test_weather_station_scenarios(sandbox):
    ws1 = WeatherStation(id='station1')
    ws2 = WeatherStation(id='station2')

    with sandbox.db() as db:
        insert_weather_station(db=db, weather_station=ws1)

        count = db.execute('SELECT COUNT(id) FROM weather_station').fetchone()
        assert count == (1,)

        insert_weather_station(db=db, weather_station=ws1)

        count = db.execute('SELECT COUNT(id) FROM weather_station').fetchone()
        assert count == (1,)

        insert_weather_station(db=db, weather_station=ws2)

        count = db.execute('SELECT COUNT(id) FROM weather_station').fetchone()
        assert count == (2,)


def test_weather_data_inserts_weather_station(sandbox):
    weather_station = WeatherStation(id='station1')
    weather_data = WeatherData(
        timestamp=datetime.datetime.now(
            zoneinfo.ZoneInfo(key='UTC'),
        ).replace(microsecond=0),
        weather_station=weather_station,
        temperature=100,
        humidity=50,
        dew_point=60,
        feels_like=110,
        absolute_pressure=30.000,
        relative_pressure=30.000,
        rainfall_rate=0.000,
        daily_rain=0.000,
        weekly_rain=0.000,
        monthly_rain=0.000,
        yearly_rain=0.000,
        wind_speed=0.00,
        wind_gust_speed=0.00,
        wind_direction=0,
        solar_radiation=0.0,
        uv_index=0,
    )

    with sandbox.db() as db:
        insert_weather_data(db=db, weather_data=weather_data)

        count = db.execute('SELECT COUNT(id) FROM weather_station').fetchone()
        assert count == (1,)
        count = db.execute(
            'SELECT COUNT(timestamp) FROM weather_data',
        ).fetchone()
        assert count == (1,)
