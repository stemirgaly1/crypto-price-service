import pytest


@pytest.mark.asyncio
async def test_healthcheck(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_get_prices_without_ticker(async_client):
    response = await async_client.get("/prices/all")
    assert response.status_code == 422  # обязательный query-параметр


@pytest.mark.asyncio
async def test_get_latest_price(async_client):
    response = await async_client.get("/prices/latest?ticker=btc_usd")
    assert response.status_code in (200, 404)
