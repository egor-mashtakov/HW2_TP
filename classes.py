from typing import Literal


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: Literal["г", "кг", "мл", "шт"]) -> None:
        self.name = name
        self.__quantity = float(quantity)
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int | float) -> None:
        float_value = float(value)
        if float_value <= .0:
            raise ValueError("Количество должно быть положительным")
        self.__quantity = float_value

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

