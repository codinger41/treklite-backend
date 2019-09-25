from tests.base import BaseTestCase
from fixtures.contestant.join_challenge import (
    join_challenge_mutation,
    join_challenge_mutation_response,
    join_challenge_not_found,
    join_challenge_not_found_response,
)
from fixtures.contestant.leave_challenge import (
    leave_challenge_mutation,
    leave_challenge_mutation_response
)

from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateContestant(BaseTestCase):

    def test_join_challenge(self):
        """
        Testing for when a contestant wants to join a challenge
        """
        execute_query = self.client.execute(
            join_challenge_mutation,
            context_value={'session': db_session})

        expected_response = join_challenge_mutation_response
        self.assertEqual(execute_query, expected_response)

    def test_join_challenge_not_found(self):
        """
        Test for when a contestant wants to join a challenge that does not exist # noqa
        """
        execute_query = self.client.execute(
            join_challenge_not_found,
            context_value={'session': db_session})

        expected_response = join_challenge_not_found_response
        self.assertEqual(execute_query, expected_response)

    def test_leave_challenge(self):
        """
        Testing for when a contestant wants to leave a challenge
        """
        execute_query = self.client.execute(
            leave_challenge_mutation,
            context_value={'session': db_session})

        expected_response = leave_challenge_mutation_response
        self.assertEqual(execute_query, expected_response)
