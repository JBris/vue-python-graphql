import aiohttp
from api.models.git_collection import GitCollection
from api.plugins.igit_plugin import IGitPlugin
from graphql import GraphQLError
from collections import OrderedDict 

class GitLab(IGitPlugin):
    endpoint="https://gitlab.com/api/v4/projects"
    session = aiohttp.ClientSession()

    def get_id(self):
        return "gitlab"

    async def search(self, project, quantity) -> GitCollection:
        
        res = await self.session.get(
            self.endpoint,
            params={ 
                'search': project, 
                'scope': "project",
                'per_page': quantity 
            } 
        )

        self.session.close()
        res_body = await res.json()        
        if res.status != 200:
            raise GraphQLError("Error: Response code: ", (res.status), " - Message: " + res_body['message'])
        else:
            git_collection = { "items": [] }
            for i, item in enumerate(res_body):
                search_result=OrderedDict()
                search_result['id'] = i
                search_result['repo'] = item['name']
                search_result['author'] = item['namespace']['path']
                search_result['host'] = "gitlab.com"
                search_result['htmlUrl'] = item['web_url']
                search_result['description'] = item['description']
                search_result['tagsUrl'] = "https://gitlab.com/api/v4/projects/" + str(item['id']) + "/repository/tags"
                search_result['cloneUrl'] = item['http_url_to_repo']
                git_collection['items'].append(search_result)
                
            return git_collection
