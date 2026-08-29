from fastapi import APIRouter, Path, HTTPException, status
from app.modules.producto.schemas import ProductoRead, ProductoCreate, ProductoStockResponse
from app.modules.producto.services import crear, listar, obtener_por_id, actualizar_total, desactivar, obtener_estado_stock

router = APIRouter(prefix="/productos", tags=["producto"])

@router.post(
    "/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED
)
async def crear_producto(data: ProductoCreate) -> ProductoRead:
    nuevo = crear(data)
    return nuevo

@router.get(
    "/", response_model = list[ProductoRead]
)
async def listar_productos(skip: int = 0, limit: int = 10) -> list[ProductoRead]:
    lista = listar(skip, limit)
    return lista

@router.get(
    "/{id}", response_model=ProductoRead
)
async def detalle_producto(id:int = Path(..., gt=0)):
    porid = obtener_por_id(id)
    if porid is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado.")
    return porid

@router.put(
    "/{id}", response_model=ProductoRead
)
async def actualizar_producto(data: ProductoCreate, id: int = Path(..., gt=0)):
    nuevo = actualizar_total(data, id)
    if nuevo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado.")
    return nuevo

@router.put(
    "/{id}/desactivar", response_model=ProductoRead
)
async def desactivar_producto(id:int = Path(..., gt=0)):
    nuevo = desactivar(id)
    if nuevo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado.")
    return nuevo

@router.get(
    "/{id}/stock", response_model=ProductoStockResponse
)
async def consultar_stock(id: int = Path(..., gt=0)) -> ProductoStockResponse:
    respuesta = obtener_estado_stock(id)
    if respuesta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado.")
    return respuesta