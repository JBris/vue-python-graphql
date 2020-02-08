from aiohttp import web

async def index(request):
    res = {"error": "Route not found."}
    return web.json_response(data=res, status=404)