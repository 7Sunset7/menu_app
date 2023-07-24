import uvicorn
from fastapi import FastAPI

from endpoints import dish, menu, submenu

app = FastAPI(title="Menu")

app.include_router(menu.router, prefix="/api/v1/menus", tags=["menus"])
app.include_router(
    submenu.router,
    prefix="/api/v1/menus/{menu_id}/submenus",
    tags=["submenus"],
)
app.include_router(
    dish.router,
    prefix="/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
    tags=["dishes"],
)


