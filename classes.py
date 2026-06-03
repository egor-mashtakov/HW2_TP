import copy
from collections import defaultdict
from typing import Literal


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: Literal["г", "кг", "мл", "шт"]) -> None:
        self.name = name
        self.quantity = float(quantity)
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

class ShoppingList:
    def __init__(self) -> None:
        self._items: list[tuple[Ingredient, str]] = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        self._items.extend((ingredient, recipe.title) for ingredient in recipe.ingredients)

    def remove_recipe(self, title: str) -> None:
        self._items = [(ing, t) for ing, t in self._items if t != title]



    def get_list(self) -> list[Ingredient]:
        totals = defaultdict(float)

        for ingredient, _ in self._items:
            key = (ingredient.name, ingredient.unit)
            totals[key] += ingredient.quantity

        ingredients = [
            Ingredient(name, quantity, unit)
            for (name, unit), quantity in totals.items()
        ]

        return sorted(ingredients, key=lambda ing: ing.name)

    def __add__(self, other: "ShoppingList") -> "ShoppingList":
        if not isinstance(other, ShoppingList):
            raise TypeError("Can combine only with ShoppingList")
        new_list = ShoppingList()
        new_list._items = copy.deepcopy(self._items) + copy.deepcopy(other._items)
        return new_list