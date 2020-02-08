from graphene.relay import Node
from app.api.queries.git_query import GitQuery

class Query(GitQuery):
    """
    The main GraphQL query point.
    """
    node = Node.Field()