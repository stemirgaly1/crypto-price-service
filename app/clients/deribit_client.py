import aiohttp

DERIBIT_URL = "https://www.deribit.com/api/v2/public/get_index_price"

async def get_index_price(currency: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(DERIBIT_URL, params={"index_name": currency}) as resp:
            data = await resp.json()
            return data["result"]["index_price"]
