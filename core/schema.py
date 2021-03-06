import graphene
from api.graphql import schema


class Query(schema.Query, graphene.ObjectType):
    pass


# class Mutation(schema.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
