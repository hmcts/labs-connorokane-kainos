import os

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/", response_class=PlainTextResponse)
async def welcome() -> str:
    return f"Welcome to your app, my favourite fruit is {os.environ['FAVOURITE_FRUIT']}"
