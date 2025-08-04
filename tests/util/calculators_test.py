from __future__ import annotations

from local_weather_server.utils.calculators import dew_pointc
from local_weather_server.utils.calculators import dew_pointf
from local_weather_server.utils.calculators import feels_like
from local_weather_server.utils.calculators import heat_index
from local_weather_server.utils.calculators import wind_chill


def test_dew_point_fahrenheit():
    assert round(dew_pointf(temperature=100, humidity=70), 1) == 88.5
    assert round(dew_pointf(temperature=90, humidity=70), 1) == 78.9


def test_dew_point_celsius():
    assert round(dew_pointc(temperature=30, humidity=70), 1) == 23.9
    assert round(dew_pointc(temperature=20, humidity=70), 1) == 14.4


def test_heat_index_fahrenheit():
    assert round(heat_index(temperature=80, humidity=45), 1) == 79.8
    assert round(heat_index(temperature=80, humidity=50), 1) == 80.8
    assert round(heat_index(temperature=85, humidity=95), 1) == 104.6
    assert round(heat_index(temperature=90, humidity=5), 1) == 84.5


def test_wind_chill_fahrenheit():
    assert round(wind_chill(temperature=40, wind_speed=15), 1) == 31.8


def test_feels_like():
    assert round(
        feels_like(
            temperature=70,
            humidity=40, wind_speed=10,
        ), 1,
    ) == 70.0
    assert round(
        feels_like(
            temperature=70,
            humidity=80, wind_speed=10,
        ), 1,
    ) == 70.5
    assert round(
        feels_like(
            temperature=83,
            humidity=10, wind_speed=10,
        ), 1,
    ) == 79.9
    assert round(
        feels_like(
            temperature=55,
            humidity=100, wind_speed=10,
        ), 1,
    ) == 55.0
    assert round(
        feels_like(
            temperature=30,
            humidity=20, wind_speed=10,
        ), 1,
    ) == 21.2
