import graphene
from graphql import ResolveInfo

from app.api.models.reviews import Review

class ReviewsQuery(graphene.ObjectType):
    review = graphene.Field(
        Review,
        id=graphene.Argument(graphene.String),
        description='A review with given id',
    )

    async def resolve(self, info: ResolveInfo):
        app = info.context['request'].app
        review = Review()
        review['author'] = "hello"
        review['project'] = "world"
        return review