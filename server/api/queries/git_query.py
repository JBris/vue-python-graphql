import graphene

from api.models.git_collection import GitCollection
from api.plugins.providers import Providers
from graphql import GraphQLError

class GitQuery(graphene.ObjectType):

    gitRepos = graphene.Field(
        GitCollection,
        provider=graphene.Argument(Providers, description="The search provider."),
        project=graphene.Argument(graphene.String, description="The name of the project"),
        quantity=graphene.Argument(graphene.Int, required=False, default_value=5, description="The number of results to return"),
        description='Git Repo information',
    )

    async def resolve_gitRepos(self, info, provider, project, quantity) -> GitCollection:
        if project == '': raise GraphQLError("Project field must not be empty.")
        app = info.context['request'].app
        search_map = app['search_map']
        if provider not in search_map: raise GraphQLError('Provider unavailable: ' + provider)
        git = search_map[provider]
        return await git.search(project, quantity)