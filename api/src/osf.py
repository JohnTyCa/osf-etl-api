import os
from aiohttp import ClientSession
from fastapi import HTTPException

async def get_collections(session: ClientSession) -> dict:
    is_next = True
    url = '{}/collections'.format(os.environ.get('OSF_URL'))
    while is_next:
        async with session.get(url) as response:
            if response.status != 200:
                print(await response.json())
                raise HTTPException(status_code=500, detail="Internal Server Error")
            response_data: dict = await response.json()
            yield response_data.get('data')
        next_url: str = response_data.get('links').get('next')
        if next_url is not None:
            url = next_url
        else:
            is_next = False
        