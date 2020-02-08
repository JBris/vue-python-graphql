from api.plugins.igit_plugin import IGitPlugin

class Bitbucket(IGitPlugin):
    def get_id(self):
        return "bitbucket"