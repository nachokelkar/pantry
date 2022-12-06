"""
Python module to track products as general items
(not necessarily in the kitchen), and a list of items.
"""

from json import load
import pymongo


class ProductHandler:
    """
    This class is the MongoDB client for the product database.
    All updates to the database happens through here.
    """
    def __init__(
        self,
        mongo_filepath: str = "login.json"
    ) -> None:
        with open(mongo_filepath, encoding='utf-8') as __credential_file:
            __credentials = load(__credential_file)
        self.__username = __credentials['username']
        self.__password = __credentials['password']

        __connection_string = "mongodb+srv://"\
            f"{self.__username}"\
            f":{self.__password}"\
            "@pantrycluster.p3drg36.mongodb.net/"\
            "?retryWrites=true&w=majority"
        __client = pymongo.MongoClient(__connection_string)
        self.__database = __client.test

    def add_product(
        self,
        product: 'Product'
    ) -> None:
        """
        Adds a product to the database.
        """
        self.__database.insert_one(product)

    def update_product(
        self,
        product: 'Product'
    ):
        """
        Updates a product using fields from the input parameter `product`.
        """
        # TODO


class Product(ProductHandler):
    """
    This class generically represents an item, as an ingredient.
    """
    def __init__(
        self,
        name: str = "",
        quantity_type: str = "",
        tags: list = None
    ) -> None:
        self.name = name
        self.quantity_type = quantity_type
        if tags is None:
            tags = []
        self.tags = tags
        self.brands = []
        self.average_price = 0.0
        self.n_samples = 0

    def __repr__(self) -> str:
        return self.name

    def add_brand(self, brand: str) -> None:
        """
        Function to add a brand to a product
        """
        self.brands.append(brand)

    def add_tag(self, tag: str) -> None:
        """
        Function to add a tag to a product
        """
        self.tags.append(tag)
