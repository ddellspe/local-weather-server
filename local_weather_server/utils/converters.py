from __future__ import annotations


def c_to_f(temperature: float) -> float:
    return temperature * 9 / 5 + 32


def f_to_c(temperature: float) -> float:
    return (temperature - 32) / 9 * 5
