from app.views import index
import pathlib

from app.api.views import gqil_view, gql_view

async def init_routes(app):
    app.router.add_route('*', '/', index)
    app.router.add_route('*', '/graphiql', gqil_view, name='graphiql')
    
    gql_resource = app.router.add_resource("/graphql")
    gql_resource.add_route("POST", gql_view)
