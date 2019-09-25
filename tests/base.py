import os
import sys

# Packages
from flask_testing import TestCase
from graphene.test import Client
from alembic import command, config

# Setup
from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base

# Models
from api.contestant.model import Contestant
from api.user.models import User
from api.challenge.models import Challenge
from api.challenge_entries.model import ChallengeEntry


sys.path.append(os.getcwd())


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:7000/graphql'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')
            user = User(fullname="doe jon",
                        username="tested",
                        email="sample@test.com")

            user.save()
            challenge = Challenge(title="zanku challenge",
                                  start_date="2019-08-15 06:00:49.303402",
                                  end_date="2019-08-15 06:00:49.303402",
                                  description="citizen@yahoo.com",
                                  image="https://picsum.photos/200",
                                  prize="10000")

            challenge.save()
            contestant = Contestant(challenge=1,
                                    contestant=2,
                                    state="subscribed")

            contestant.save()
            challenge_entry = ChallengeEntry(contestant_id=2,
                                             challenge_id=1,
                                             file_url="http://foobar.hj")
            challenge_entry.save()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
