import api.user.schema


from graphene import Schema


class Mutation(
    api.user.schema.Mutation
):
    """Root for politico Graphql queries"""
    pass


class Query(
    api.user.schema.Query
):
    """Root for converge Graphql queries"""
    pass


schema = Schema(mutation=Mutation, query=Query)
