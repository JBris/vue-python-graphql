import aiohttp
from api.models.git_collection import GitCollection
from api.plugins.igit_plugin import IGitPlugin
from graphql import GraphQLError
from collections import OrderedDict 

class Bitbucket(IGitPlugin):
    endpoint="https://api.github.com/search/repositories"
    session = aiohttp.ClientSession()

    def get_id(self):
        return "bitbucket"

    async def search(self, project, quantity) -> GitCollection:
        return {"items": [{ 'author':'foo', 'project': 'bar', 'provider': self.get_id() }]}