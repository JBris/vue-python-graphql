import graphene

class Providers(graphene.Enum):
    GITHUB = 'github'
    GITLAB = 'gitlab'
    BITBUCKET = 'bitbucket'
    