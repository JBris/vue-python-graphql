from api.models.git_collection import GitCollection
from yapsy.IPlugin import IPlugin

class IGitPlugin(IPlugin):
    
    def get_id(self):
        raise NotImplementedError("Git Plugin must have an ID.")

    async def search(self, project, quantity) -> GitCollection:
        raise NotImplementedError("Git Plugin must implement a search method.")