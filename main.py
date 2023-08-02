from fastapi.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI

from app.routers import tenant_crud, tenant_show

app = FastAPI()
app.include_router(tenant_crud.router)
app.include_router(tenant_show.router)

api_version = "1.0.0"


@app.get("/")
def root():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/version")
async def get_version():
    return {"version": api_version}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
