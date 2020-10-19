from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from .graph import schema
from .mongo import init_database, finalize_database


app = FastAPI()


app.add_route("/", GraphQLApp(schema=schema))


@app.on_event('startup')
async def on_startup():
    await init_database()


@app.on_event('shutdown')
async def on_shutdown():
    await finalize_database()
