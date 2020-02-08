from aiohttp import web
from routes import init_routes
from yapsy.PluginManager import PluginManager

app = web.Application()
manager = PluginManager()
manager.setPluginPlaces(["/app/api/plugins"])
manager.collectPlugins()

search_list = []
search_map = {}
for plugin in manager.getAllPlugins():
    plugin_object = plugin.plugin_object
    search_list.append(plugin_object)
    search_map[plugin_object.get_id()] = plugin_object

app['search_list'] = search_list
app['search_map'] = search_map

print(app['search_list'] )
print(app['search_map'] )

init_routes(app)