import pytest
from app.services.price_service import PriceService


@pytest.mark.asyncio
async def test_price_service_creation():
    service = PriceService()
    assert service is not None
