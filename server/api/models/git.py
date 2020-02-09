import graphene

class Git(graphene.ObjectType):
    id = graphene.String()
    repo = graphene.String()
    author = graphene.String()
    host = graphene.String()
    htmlUrl = graphene.String()
    tagsUrl = graphene.String()
    cloneUrl = graphene.String()
    description = graphene.String()
