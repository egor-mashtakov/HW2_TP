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


def test_recipe_creation():
    ing1 = Ingredient("Крот", 1.0, "шт")
    ing2 = Ingredient("Спирт", 600.0, "мл")
    recipe = Recipe("Кротовуха", [ing1, ing2])

    assert recipe.title == "Кротовуха"
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].name == "Крот"


def test_recipe_add_ingredient():
    recipe = Recipe("Блинчики", [])
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 200.0, "г")
    ing3 = Ingredient("Сахар", 100.0, "г")

    recipe.add_ingredient(ing1)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 500.0

    recipe.add_ingredient(ing2)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 700.0

    recipe.add_ingredient(ing3)
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[1].quantity == 100
    assert recipe.ingredients[1].name == "Сахар"


def test_recipe_scale():
    ing1 = Ingredient("Крот", 600.0, "мл")
    recipe = Recipe("Кротовуха", [ing1])

    scaled_recipe = recipe.scale(2.0)

    assert scaled_recipe is not recipe
    assert scaled_recipe.title == "Кротовуха"
    assert scaled_recipe.ingredients[0].quantity == 1200.0
    assert recipe.ingredients[0].quantity == 600.0

    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-1.5)


def test_recipe_len():
    ing1 = Ingredient("Спирт", 500.0, "мл")
    ing2 = Ingredient("Спирт", 700.0, "мл")
    ing3 = Ingredient("Крот", 1.0, "шт")

    recipe = Recipe("Кротовуха", [ing1, ing2, ing3])
    assert len(recipe) == 2
