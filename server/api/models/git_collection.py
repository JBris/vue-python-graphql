import graphene
from api.models.git import Git

class GitCollection(graphene.ObjectType):
    items = graphene.List(graphene.NonNull(Git))
    