import time
from app.tasks.celery_app import celery_app
from app.clients.deribit_client import get_index_price
from app.db.session import AsyncSessionLocal
from app.db.models import Price

@celery_app.task
def fetch_prices():
    import asyncio

    async def run():
        async with AsyncSessionLocal() as session:
            for ticker in ["btc_usd", "eth_usd"]:
                price = await get_index_price(ticker)
                session.add(
                    Price(
                        ticker=ticker,
                        price=price,
                        timestamp=int(time.time())
                    )
                )
            await session.commit()

    asyncio.run(run())
