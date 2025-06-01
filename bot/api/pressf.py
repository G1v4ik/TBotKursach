from yarl import URL

from os import getenv
from dotenv import load_dotenv

import httpx

from bot.schames import schames


class PressFClient:

    def __init__(
            self, base_url: URL
    ):
        self._base_url = base_url
        self._client = httpx.AsyncClient()
   

    async def create(
            self,
            schames_input: schames.BaseModel,
            endpoint: str
    ) -> httpx.Response:
        
        resp = await self._client.post(
            f"{self._base_url}{endpoint}",
            json=schames_input.model_dump()
        )
        print (f"{self._base_url}{endpoint}")
        return resp

    async def get(
            self,
            schames_output: schames.BaseModel,
            endpoint: str,
            id_object: int
    ) -> httpx.Response:
        
        resp = await self._client.get(
            f"{self._base_url}{endpoint}{id_object}"
        )
        
        return resp


    async def list(
              self,
              schames_output: schames.BaseModel,
              endpoint: str
    ) -> httpx.Response:
         
        resp = await self._client.get(
            f"{self._base_url}{endpoint}"
        )
        return resp
    

    async def patch(
                self,
                id_message: int,
                endpoint: str
    ) -> httpx.Response:
        resp = await self._client.patch(
            f"{self._base_url}{endpoint}",
            json={"id_message": id_message}
        )
        return resp


load_dotenv()
base_url = getenv('BASE_URL_API')
Client = PressFClient(base_url)