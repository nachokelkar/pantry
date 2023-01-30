"""
This module keeps track of the grocery list.
"""
import boto3


class GroceryListHandler:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name="us-east-1"
        )
        self.table = self.dynamodb.Table('grocery-list')

    def get_list(self, user):
        """
        Gets grocery list of the user
        """

        # Get the response
        response_table = self.table.get_item(
            Key={
                "username": user
            },
            AttributesToGet=[
                "grocery_list",
            ]
        )

        try:
            grocery_list = []
            for item in response_table['Item']['grocery_list']:
                grocery_list.append(item['item'])
            return grocery_list
        except KeyError:
            return []

    def update_item(self, user, item):
        """
        Adds item to grocery list if it doesn't exist
        """

        # Set update expression
        update_expr = """
        SET grocery_list = list_append(if_not_exists(grocery_list, :e), :item)
        """

        # Add item to list
        self.table.update_item(
            Key={
                "username": user
            },
            UpdateExpression=update_expr,
            ExpressionAttributeValues={
                ':e': [],
                ':item': [item],
            }
        )

        return {"added": item}

    def remove_item(self, user, item):
        """
        Removes an item from the user's grocery list.
        """

        # Fetch grocery_list
        response_table = self.table.get_item(
            Key={
                "username": user
            },
            AttributesToGet=[
                "grocery_list",
            ]
        )

        # Get list items
        response = response_table.get('Item', {}).get('grocery_list', [])

        # Find item index
        for i, key in enumerate(response):
            if key['item'] == item:
                item_index = i

        # Remove item
        self.table.update_item(
            Key={
                "username": user
            },
            UpdateExpression=f"REMOVE grocery_list[{item_index}]"
        )

        return {"removed": item}
