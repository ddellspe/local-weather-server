from __future__ import annotations

from math import log
from math import sqrt
from typing import Final

from local_weather_server.utils.converters import c_to_f
from local_weather_server.utils.converters import f_to_c

B: Final[float] = 243.04
A: Final[float] = 17.625


def alpha(temperature: float, humidity: float) -> float:
    return log(humidity / 100) + ((A * temperature) / (B + temperature))


def dew_pointf(temperature: float, humidity: float) -> float:
    return c_to_f(
        dew_pointc(f_to_c(temperature=temperature), humidity=humidity),
    )


def dew_pointc(temperature: float, humidity: float) -> float:
    return ((B * alpha(temperature=temperature, humidity=humidity)) /
            (A - alpha(temperature=temperature, humidity=humidity)))


def wind_chill(temperature: float, wind_speed: float) -> float:
    return (
        35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16)
        + 0.4275 * temperature * (wind_speed ** 0.16)
    )


def steadman_heat_index(temperature: float, humidity: float) -> float:
    return (
        0.5 * (
            temperature + 61 + ((temperature - 68) * 1.2)
            + (humidity * 0.094)
        )
    )


def low_heat_index_adjustment(temperature: float, humidity: float) -> float:
    return (((humidity - 85) / 10) * ((87 - temperature) / 5))


def high_heat_index_adjustment(temperature: float, humidity: float) -> float:
    return (
        ((13 - humidity) / 4) * sqrt((17 - abs(temperature - 95)) / 17)
    )


def rothfusz_heat_index(temperature: float, humidity: float) -> float:
    return (
        -42.379 + 2.04901523 * temperature
        + 10.14333127 * humidity
        - 0.22475541 * temperature * humidity
        - 0.00683783 * temperature * temperature
        - 0.05481717 * humidity * humidity
        + 0.00122874 * temperature * temperature * humidity
        + 0.00085282 * temperature * humidity * humidity
        - 0.00000199 * temperature * temperature * humidity * humidity
    )


def heat_index(temperature: float, humidity: float) -> float:
    heat_index: float = steadman_heat_index(
        temperature=temperature, humidity=humidity,
    )
    if heat_index < 80.0:
        return heat_index
    heat_index = rothfusz_heat_index(
        temperature=temperature, humidity=humidity,
    )
    if humidity <= 13 and 80 <= temperature <= 112:
        heat_index = (
            heat_index -
            high_heat_index_adjustment(
                temperature=temperature, humidity=humidity,
            )
        )
    elif humidity > 85 and 80 <= temperature <= 87:
        heat_index = (
            heat_index +
            low_heat_index_adjustment(
                temperature=temperature, humidity=humidity,
            )
        )
    return heat_index


def feels_like(
        temperature: float,
        humidity: float,
        wind_speed: float,
) -> float:
    if temperature >= 80 or (temperature >= 60 and humidity >= 50):
        return heat_index(temperature=temperature, humidity=humidity)
    elif temperature <= 40:
        return wind_chill(temperature=temperature, wind_speed=wind_speed)
    else:
        return temperature
