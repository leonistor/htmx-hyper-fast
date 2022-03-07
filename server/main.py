from fastapi import FastAPI

from routes.htmx_click_edit import router as router_htmx_click_edit


app = FastAPI()
app.include_router(router_htmx_click_edit, prefix="/api")
