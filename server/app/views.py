from aiohttp import web

async def index(request):
    res = { "message": "Please use the /graphql and /graphiql endpoints." }
    return web.json_response(data=res)