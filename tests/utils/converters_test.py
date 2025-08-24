from __future__ import annotations

from local_weather_server.utils.converters import c_to_f
from local_weather_server.utils.converters import f_to_c


def test_f_to_c():
    assert 0 == f_to_c(32)
    assert 100 == f_to_c(212)
    assert -40 == f_to_c(-40)


def test_c_to_f():
    assert 32 == c_to_f(0)
    assert 212 == c_to_f(100)
    assert -40 == c_to_f(-40)
