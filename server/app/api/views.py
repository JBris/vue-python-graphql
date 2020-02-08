import graphene
import asyncio
from graphql.execution.executors.asyncio import AsyncioExecutor

from aiohttp_graphql import GraphQLView
from app.api.queries import Query

schema = graphene.Schema(
    query=Query,
)

gqil_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    graphiql=True,
    enable_async=True,
)

gql_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    graphiql=False,
    enable_async=True,
)