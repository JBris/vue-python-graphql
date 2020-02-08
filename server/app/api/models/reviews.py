import graphene

class Review(graphene.ObjectType):
    author = graphene.String()
    project = graphene.String()