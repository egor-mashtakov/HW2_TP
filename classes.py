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


class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]) -> None:
        self.title = title
        self.ingredients = []
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def add_ingredient(self, ingredient: Ingredient) -> None:
        for item in self.ingredients:
            if item == ingredient:
                item.quantity += ingredient.quantity
                return

        self.ingredients.append(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))

    @staticmethod
    def is_valid_ratio(ratio: int | float) -> bool:
        if not isinstance(ratio, (int, float)):
            return False
        return ratio > .0

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Ratio must be positive number")

        scaled_ingredients = []
        for ingredient in self.ingredients:
            scaled_ingredients.append(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return Recipe(self.title, scaled_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return self.title + "\n" + "\n".join(str(ingredient) for ingredient in self.ingredients)
