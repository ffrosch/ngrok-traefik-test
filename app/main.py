from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"message": "hello world", "headers": request.headers}

# Catch-all route
@app.get("/{path:path}")
async def catch_all(path: str, request: Request):
    return {"message": f"The path '{path}' was not found on this server.", "headers": request.headers}
