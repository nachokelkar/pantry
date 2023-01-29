"""
This module keeps track of the grocery list.
"""
import boto3


class GroceryListHandler:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('users')

    def update_item(self, user, item):
        self.table.update_item(
            Key={
                "username": user
            },
            UpdateExpression="SET list = list_append(list, :item)",
            ExpressionAttributeValues={
                ':item': [item],
            }
        )

    def remove_item(self, user, item):
        self.table.update_item(
            Key={
                "username": user
            },
            UpdateExpression="REMOVE list :item",
            ExpressionAttributeValues={
                ':item': [item],
            }
        )
