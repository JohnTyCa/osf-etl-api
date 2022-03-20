from aiohttp import ClientSession
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from . import osf

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
origins = [
    'http://localhost:5000',
    'http://localhost:3000',
    'http://localhost:80',
    'http://localhost'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

async def yield_session():
    session = ClientSession()
    try:
        yield session
    finally:
        await session.close()

@app.get('/public-collections')
async def retrieve_all_collections_that_are_publically_available_on_osf(
    session = Depends(yield_session),
):
    collections = []
    async for data in  osf.get_collections(session):
        collections = [*collections, *data]
    return collections
