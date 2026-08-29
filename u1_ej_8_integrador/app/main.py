from fastapi import FastAPI
from app.modules.categoria.routers import router as categoria_router
from app.modules.producto.routers import router as producto_router

def crear_app():
    app = FastAPI(
        title="API Integradora - Unidad 1",
        description="Conceptos: Path, Query, Body, Pydantic, Errores.",
        version="1.0.0"
    )
    app.include_router(categoria_router)
    app.include_router(producto_router)

    return app

app = crear_app()