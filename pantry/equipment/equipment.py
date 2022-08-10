"""
This module holds the class of an equipment in the kitchen,
such as a grinder, fridge, oven, etc.
"""

class Equipment:
    """
    Generic class for equipment in the kitchen.
    """
    def __init__(
        self,
        name:str,
        tags:list
    ) -> None:
        self.name = name
        self.tags = tags

    def __repr__(self) -> str:
        return self.name
