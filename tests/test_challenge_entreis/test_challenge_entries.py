from tests.base import BaseTestCase
from fixtures.challenge_entries.entries import (
    create_challenge_entry_mutation,
    create_challenge_entry_mutation_reponse,
    create_challenge_entry_contestant_not_found,
    create_challenge_entry_not_found_contestant_response,
    create_challenge_entry_challenge_not_found,
    create_challenge_entry_challenge_not_found_reponse,
    create_challenge_entry_challenge_invalid_file_url,
    create_challenge_entry_challenge_invalid_file_url_response,
)
from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestChallengeEntry(BaseTestCase):

    def test_create_challenge_entry_mutation(self):
        """
        Testing for when a contestant wants to submit an entry for a challenge
        """
        execute_query = self.client.execute(
            create_challenge_entry_mutation,
            context_value={'session': db_session})

        expected_response = create_challenge_entry_mutation_reponse
        self.assertEqual(execute_query, expected_response)

    def test_create_challenge_entry_contestant_not_found(self):
        """
        Test for when a contestant that does not exist wants to join a challenge # noqa
        """
        execute_query = self.client.execute(
            create_challenge_entry_contestant_not_found,
            context_value={'session': db_session})

        expected_response = create_challenge_entry_not_found_contestant_response
        self.assertEqual(execute_query, expected_response)

    def test_create_challenge_entry_challenge_not_found(self):
        """
        Test for when a contestant tries to join a challenge that does not exist
        """
        execute_query = self.client.execute(
            create_challenge_entry_challenge_not_found,
            context_value={'session': db_session})

        expected_response = create_challenge_entry_challenge_not_found_reponse
        self.assertEqual(execute_query, expected_response)

    def test_create_challenge_entry_challenge_invalid_file_url(self):
        """
        Test for when a contestant tries to submit an invalid url entry
        """
        execute_query = self.client.execute(
            create_challenge_entry_challenge_invalid_file_url,
            context_value={'session': db_session})

        expected_response = create_challenge_entry_challenge_invalid_file_url_response # noqa
        self.assertEqual(execute_query, expected_response)
