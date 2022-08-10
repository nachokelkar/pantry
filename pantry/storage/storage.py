"""
This module holds the class of a storage space in the kitchen,
such as a fridge, cabinet, etc.
"""
from typing import List

from pantry.equipment.equipment import Equipment

class Storage(Equipment):
    """
    Generic class for a storage space. This was created to store
    a list of items that are in the space, and to separate from
    the equipment class.
    """
    def __init__(
        self,
        name: str,
        tags: list,
        kind: str,
        items: List[str]
    ) -> None:
        super().__init__(name, tags)
        self.kind = kind
        self.items = items

    def __getitem__(self, index):
        return self.items[index]
