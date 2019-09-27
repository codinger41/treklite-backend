import api.user.schema
import api.trip.schema

from graphene import Schema


class Mutation(
    api.user.schema.Mutation,
    api.trip.schema.Mutation
):
    """Root for politico Graphql queries"""
    pass


class Query(
    api.user.schema.Query,
    api.trip.schema.Query
):
    """Root for converge Graphql queries"""
    pass


schema = Schema(mutation=Mutation, query=Query)
