"""
Module to track pantry of a kitchen.
Includes inventory, recipes, etc.
"""

class Item:
    """
    Class to capture an item.
    Can have complex quantities (exact amounts) or simple ("a lot", "about half", "not much").
    Includes tags.
    """
    def __init__(self) -> None:
        pass

class Recipe:
    """
    Class to store a recipe.
    Includes instructions as a string, equipment needed, tags, ingredients.
    """
    def __init__(self) -> None:
        pass

class StorageUnit:
    """
    Class to capture where stuff is stored.
    Includes tags.
    """
    def __init__(self) -> None:
        pass

class Equipment:
    """
    Class to store a particular piece of equipment (oven, fridge, freezer, etc).
    """
    def __init__(self) -> None:
        pass