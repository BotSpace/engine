import asyncio
import logging
import httpx
import os


async def on_request(request):
    request.headers["Authorization"] = f"Bearer {os.getenv("API_TOKEN")}"
    print("on request")


async def fetch_async(method, url, data=None):
    api_url = os.getenv("API_URL")
    if api_url is None:
        logging.error("API_URL not found for .env")
        raise Exception("API_URL not found for .env")
    async with httpx.AsyncClient(
        base_url=api_url, event_hooks={"request": [on_request]}
    ) as client:
        response = await client.request(method, url, data=data)
        return response


async def query(collection, action, data):
    response = await fetch_async(
        "POST",
        f"/api/collection/{collection}/query/?action={action}",
        data=data,
    )
    return response


async def create_user_not_exists(chat_id, first_name, last_name):
    user = await get_user(chat_id)
    if user is not None:
        return True
    response = await query(
        "users",
        "insert",
        {
            "chat_id": chat_id,
            "first_name": first_name,
            "last_name": last_name,
        },
    )
    return response.json()["status"]


async def get_user(chat_id):
    response = await query(
        "users",
        "find_one",
        {
            "where": {
                "chat_id": chat_id,
            }
        },
    )
    data = response.json()
    if data["status"] is True:
        return data["data"]
    return None


print(asyncio.run(create_user_not_exists("12121", "Samandar", "Azamov")))
