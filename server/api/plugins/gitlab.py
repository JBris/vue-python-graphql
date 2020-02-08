from api.plugins.igit_plugin import IGitPlugin

class GitLab(IGitPlugin):
    def get_id(self):
        return "gitlab"