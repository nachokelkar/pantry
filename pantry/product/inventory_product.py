"""
Python module to track products as parts of the inventory
of a kitchen.
"""

from pantry.product.product import Product


class InventoryProduct(Product):
    """
    This class represents an item present in the kitchen,
    with the amount available, expiry, brand, etc.
    """
    def __init__(
        self,
        name: str = "",
        quantity_type: str = "",
        tags: list = None,
        brand: str = ""
    ) -> None:
        super().__init__(name, quantity_type, tags)
        self.brand = brand
