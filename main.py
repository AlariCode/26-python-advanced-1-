# def safe_div(a: float, b: float) -> Union[float, str]

from typing import TypeVar


def safe_div(a: float, b: float) -> float | str:
    if b == 0:
        return "деление на 0"
    return a / b


def safe_div2(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


T = TypeVar("T")


def ensure_list(value: T | list[T]) -> list[T]:
    if isinstance(value, list):
        return value
    return [value]
