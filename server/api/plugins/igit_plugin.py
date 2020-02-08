from yapsy.IPlugin import IPlugin

class IGitPlugin(IPlugin):
    
    def get_id(self):
        raise NotImplementedError("Git Plugin must have an ID.")