import graphene

from app.api.models.git import Git
from app.api.models.providers import Providers

class GitQuery(graphene.ObjectType):
    gitRepo = graphene.Field(
        Git,
        provider=graphene.Argument(Providers),
        project=graphene.Argument(graphene.String),
        description='Git Repo information',
    )

    def resolve_gitRepo(self, info, project, provider) -> Git:
        return { 'author':'foo', 'project': 'bar', 'provider': 'baz'}