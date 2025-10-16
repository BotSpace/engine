import asyncio
import logging
import httpx
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


async def on_request(request: httpx.Request):
    request.headers["Authorization"] = f"Bearer {os.getenv("API_TOKEN")}"
    logging.info("on_request content=%s url=%s", request.content, request.url)


async def on_response(response: httpx.Response):
    level = logging.INFO
    if response.status_code >= 400:
        level = logging.ERROR
    logging.log(
        level, "on_response data=%s url=%s", await response.aread(), response.url
    )


async def fetch_async(method, url, data=None):
    api_url = os.getenv("API_URL")
    if api_url is None:
        logging.error("API_URL not found for .env")
        raise Exception("API_URL not found for .env")
    async with httpx.AsyncClient(
        base_url=api_url,
        event_hooks={"request": [on_request], "response": [on_response]},
    ) as client:
        response = await client.request(method, url, json=data)
        return response


async def query(collection, action, data):
    project_id = os.getenv("PROJECT_ID")
    if project_id is None:
        logging.error("API_URL not found for .env")
        raise Exception("API_URL not found for .env")
    response = await fetch_async(
        "POST",
        f"/api/collection/{collection}/query/?action={action}&project={project_id}",
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
