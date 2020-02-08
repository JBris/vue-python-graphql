from aiohttp import web
from routes import init_routes
from yapsy.PluginManager import PluginManager

app = web.Application()
manager = PluginManager()
manager.setPluginPlaces(["/app/api/plugins"])
manager.collectPlugins()

for plugin in manager.getAllPlugins():
    plugin.plugin_object.print_name()

init_routes(app)