import re
import validators
from graphql import GraphQLError


def verify_email(email):
    return bool(re.match('^.+@(\[?)[a-zA-Z0-9-.]+.', email))  # noqa


def validate_url(**kwargs):
    """
    Function to validate url when
    saving an object
    :params kwargs
    """
    if not validators.url(kwargs.get('file_url')):
        raise AttributeError("Please enter a valid url")


class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, entity_name, entity):
        # Database integrity error
        raise GraphQLError(
            '{} {} already exists'.format(entity_name, entity))

    def foreign_key_conflict(self, entity_name, entity):
        # Database foreign key error
        raise GraphQLError(
            '{} {} does not exists'.format(entity_name, entity))

    def db_connection(self):
        # Database connection error
        raise GraphQLError('Error: Could not connect to Db')
