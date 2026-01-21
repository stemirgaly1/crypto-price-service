from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.services.price_service import PriceService

router = APIRouter(prefix="/prices", tags=["prices"])

@router.get("/all")
async def get_all_prices(
    ticker: str = Query(..., description="Currency ticker, e.g. BTC or ETH")
):
    return {
        "ticker": ticker,
        "data": []
    }

@router.get("/latest")
async def get_latest_price(ticker: str, session: AsyncSession = Depends(get_session)):
    return await PriceService.get_latest(session, ticker)

@router.get("/by-date")
async def get_prices_by_date(
    ticker: str,
    date_from: int,
    date_to: int,
    session: AsyncSession = Depends(get_session)
):
    return await PriceService.get_by_date(session, ticker, date_from, date_to)
