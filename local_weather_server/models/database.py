from __future__ import annotations

import datetime
import zoneinfo
from typing import NamedTuple

from local_weather_server.utils.calculators import dew_pointf
from local_weather_server.utils.calculators import feels_like


class WeatherStation(NamedTuple):
    identifier: str
    timezone: datetime.tzinfo | None = None


class WeatherData(NamedTuple):
    timestamp: datetime.datetime
    weather_station: WeatherStation
    temperature: float
    humidity: float
    dew_point: float
    feels_like: float
    absolute_pressure: float
    relative_pressue: float
    rainfall_rate: float
    daily_rain: float
    weekly_rain: float
    monthly_rain: float
    yearly_rain: float
    wind_speed: float
    wind_gust_speed: float
    wind_direction: float
    solar_radiation: float
    uv_index: int

    @classmethod
    def from_wungerground_request(
        cls,
        dateutc: str,
        ID: str,
        tempf: str,
        humidity: str,
        winddir: str,
        windgustmph: str,
        windspeedmph: str,
        rainin: str,
        dailyrainin: str,
        weeklyrainin: str,
        monthlyrainin: str,
        yearlyrainin: str,
        solarradiation: str,
        UV: str,
        absbaromin: str,
        baromin: str,
        *args: str,
        **kwargs: str,
    ) -> WeatherData:
        timezone = kwargs.get('timezone', 'UTC')
        tz = zoneinfo.ZoneInfo(key=timezone)
        if dateutc == 'now':
            timestamp = datetime.datetime.now(tz)
        else:
            timestamp = datetime.datetime.strptime(
                dateutc, '%Y-%m-%d %H:%M:%S',
            ).replace(tzinfo=tz)
        temperature = float(tempf)
        relative_humidity = float(humidity)
        wind_speed = float(windspeedmph)
        dew_pt = dew_pointf(
            temperature=temperature,
            humidity=relative_humidity,
        )
        feels_lk = feels_like(
            temperature=temperature,
            humidity=relative_humidity, wind_speed=wind_speed,
        )
        return WeatherData(
            timestamp=timestamp,
            weather_station=WeatherStation(identifier=ID, timezone=tz),
            temperature=temperature,
            humidity=relative_humidity,
            dew_point=round(dew_pt, 1),
            feels_like=round(feels_lk, 1),
            absolute_pressure=float(absbaromin),
            relative_pressue=float(baromin),
            rainfall_rate=float(rainin),
            daily_rain=float(dailyrainin),
            weekly_rain=float(weeklyrainin),
            monthly_rain=float(monthlyrainin),
            yearly_rain=float(yearlyrainin),
            wind_speed=wind_speed,
            wind_gust_speed=float(windgustmph),
            wind_direction=float(winddir),
            solar_radiation=float(solarradiation),
            uv_index=int(UV),
        )
