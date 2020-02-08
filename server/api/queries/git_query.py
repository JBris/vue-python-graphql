import graphene

from api.models.git import Git
from api.plugins.providers import Providers

class GitQuery(graphene.ObjectType):

    gitRepo = graphene.Field(
        Git,
        provider=graphene.Argument(Providers),
        project=graphene.Argument(graphene.String),
        description='Git Repo information',
    )

    async def resolve_gitRepo(self, info, project, provider) -> Git:
        return { 'author':'foo', 'project': 'bar', 'provider': Providers.GITHUB.value}