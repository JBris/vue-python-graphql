from graphene.relay import Node

from app.api.queries.reviews import ReviewsQuery


class Query(ReviewsQuery):
    """
    The main GraphQL query point.
    """
    node = Node.Field()