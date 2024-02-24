from typing import Union


class Calculator:
    @staticmethod
    def divide(x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arg must be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    @staticmethod
    def add(x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arg must be numeric")
        return x + y
