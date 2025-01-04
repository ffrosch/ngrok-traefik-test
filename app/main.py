from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


def headers(request: Request):
    return {
        "headers": {
            key: value
            for key, value in request.headers.items()
            if key.startswith("x-") or key == "host"
        }
    }


def url_scheme(request: Request):
    if request.url.scheme == "https":
        return {"scheme": "You are using HTTPS behind the router!"}
    else:
        return {"scheme": "You are NOT using HTTPS behind the router!"}


def ngrok_url():
    ngrok_url = os.environ.get("NGROK_DOMAIN")
    ngrok_url = "https://" + ngrok_url if ngrok_url else None
    return {"ngrok_url": ngrok_url}


@app.get("/")
async def read_root(request: Request):
    return {
        "message": "hello world",
        **headers(request),
        **url_scheme(request),
        **ngrok_url(),
    }


# Catch-all route
@app.get("/{path:path}")
async def catch_all(path: str, request: Request):
    return {
        "message": f"The path '{path}' was not found on this server.",
        **headers(request),
        **url_scheme(request),
        **ngrok_url(),
    }
