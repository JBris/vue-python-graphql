import pathlib
from views import index
import aiohttp_cors
from api.views import gqil_view, gql_view

def init_routes(app):
    app.router.add_route('*', '/', index)
    app.router.add_route('*', '/graphiql', gqil_view, name='graphiql')
    
    cors = aiohttp_cors.setup(app)
    gql_resource = cors.add(app.router.add_resource("/graphql"), {
        "*": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
            allow_credentials=True,
            allow_methods=["POST", "PUT", "GET"]),
    })

    gql_resource.add_route("POST", gql_view)
