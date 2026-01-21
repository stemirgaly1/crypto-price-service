from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Price

class PriceService:

    @staticmethod
    async def get_all(session: AsyncSession, ticker: str):
        result = await session.execute(
            select(Price).where(Price.ticker == ticker)
        )
        return result.scalars().all()

    @staticmethod
    async def get_latest(session: AsyncSession, ticker: str):
        result = await session.execute(
            select(Price)
            .where(Price.ticker == ticker)
            .order_by(Price.timestamp.desc())
            .limit(1)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_date(
        session: AsyncSession,
        ticker: str,
        date_from: int,
        date_to: int
    ):
        result = await session.execute(
            select(Price)
            .where(
                Price.ticker == ticker,
                Price.timestamp >= date_from,
                Price.timestamp <= date_to
            )
        )
        return result.scalars().all()
