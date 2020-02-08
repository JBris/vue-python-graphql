import graphene

class Git(graphene.ObjectType):
    provider = graphene.String()
    project = graphene.String()
    author = graphene.String()
    
    