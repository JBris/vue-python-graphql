import aiohttp
import asyncio

from api.models.git_collection import GitCollection
from api.plugins.igit_plugin import IGitPlugin
from bs4 import BeautifulSoup
from graphql import GraphQLError
from collections import OrderedDict 

class Bitbucket(IGitPlugin):
    url = "https://bitbucket.org/repo/all"
    endpoint = "https://api.bitbucket.org/2.0/repositories"    
    session = aiohttp.ClientSession()

    def get_id(self):
        return "bitbucket"

    async def search(self, project, quantity) -> GitCollection:        
        links = []
        tasks = []
        pages = int(quantity / 10 + 2 )  

        for page in range(1, pages): 
            tasks.append(self.session.get(
                self.url + "/" + str(page),
                params={ 'name': project } 
            ))

        responses = await asyncio.gather(*tasks, return_exceptions=True)
        self.session.close()

        for res in responses:
            content = await res.text() 
            soup = BeautifulSoup(content, 'html.parser')
            content_links = soup.findAll("a", {"class" : "repo-link" })
            for link in content_links:
                links.append(link)   
        
        length = len(links)
        git_collection = { "items": [] }
        if length == 0:
            return git_collection 

        if length > quantity:
            remainder = quantity - ((pages - 1) * 10)
            links = links[:remainder]

        tasks = []
        for link in links:
            repo = link['href']
            tasks.append(self.session.get(self.endpoint + repo))

        responses = await asyncio.gather(*tasks, return_exceptions=True)
        self.session.close()

        i = 0
        for res in responses:        
            res_body = await res.json()
            if res.status != 200:
                raise GraphQLError("Error: Response code: ", (res.status), " - Message: " + res_body['error']['message'])
            else:
                search_result=OrderedDict()
                search_result['id'] = i
                search_result['repo'] = res_body['name']
                search_result['author'] = res_body['owner'].get('nickname')
                if search_result['author'] is None : search_result['author'] = res_body['owner'].get('username') 
                search_result['host'] = "bitbucket.org"
                search_result['htmlUrl'] = res_body['links']['html']['href']
                search_result['description'] = res_body['description']
                search_result['tagsUrl'] = res_body['links']['tags']['href']
                search_result['cloneUrl'] = res_body['links']['clone'][0]['href']
                git_collection['items'].append(search_result)
                i += 1

        return git_collection
