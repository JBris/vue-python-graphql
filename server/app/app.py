from aiohttp import web
from app.routes import init_routes

app = web.Application()
app.on_startup.append(init_routes)
