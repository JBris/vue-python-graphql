import aiohttp
from api.models.git_collection import GitCollection
from api.plugins.igit_plugin import IGitPlugin
from graphql import GraphQLError
from collections import OrderedDict 

class GitHub(IGitPlugin):
    endpoint="https://api.github.com/search/repositories"
    session = aiohttp.ClientSession()

    def get_id(self):
        return "github"

    async def search(self, project, quantity) -> GitCollection:
        
        res = await self.session.get(
            self.endpoint,
            params={
                'q': project,
                'per_page': quantity
            } 
        )

        self.session.close()
        res_body = await res.json()        
        if res.status != 200:
            raise GraphQLError("Error: Response code: ", (res.status), " - Message: " + res_body['message'])
        else:
            git_collection = { "items": [] }
            for item in res_body['items']:
                search_result=OrderedDict()
                search_result['id'] = item['name']
                search_result['repo'] = item['name']
                search_result['author'] = item['owner']['login']
                search_result['host'] = "github.com"
                search_result['htmlUrl'] = item['html_url']
                search_result['description'] = item['description']
                search_result['tagsUrl'] = item['tags_url']
                search_result['cloneUrl'] = item['clone_url']
                git_collection['items'].append(search_result)

            return git_collection
