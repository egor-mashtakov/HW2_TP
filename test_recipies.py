import pytest
from classes import Ingredient, Recipe, ShoppingList


def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"
    assert isinstance(ing.quantity, float)


def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"


def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 1000.0, "г")
    ing3 = Ingredient("Сахар", 500.0, "г")
    ing4 = Ingredient("Мука", 500.0, "кг")

    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4
    assert ing1 != ""