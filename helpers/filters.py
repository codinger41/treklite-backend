from graphql import GraphQLError
from api.challenge.schema import Challenge
from api.contestant.schema import Contestant


def filter_challenge_id(info, id):
    query_challenge = Challenge.get_query(info)

    challenge = query_challenge.filter_by(id=id).first()
    if not challenge:
        raise GraphQLError("Challenge not found")


def filter_contestants_by_id(info, id):
    query_contestant = Contestant.get_query(info)
    contestant = query_contestant.filter_by(id=id).first()
    if not contestant:
        raise GraphQLError("Contestant not found")
