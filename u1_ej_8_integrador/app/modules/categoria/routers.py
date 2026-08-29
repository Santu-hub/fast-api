from fastapi import APIRouter, status, Path, HTTPException
from app.modules.categoria.schemas import CategoriaRead, CategoriaCreate
from app.modules.categoria.services import crear, listar, obtener_por_id, actualizar_total, desactivar
router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post(
    "/", response_model = CategoriaRead, status_code=status.HTTP_201_CREATED
)
async def crear_categoria(categoria: CategoriaCreate) -> CategoriaRead:
    nuevo = crear(categoria)
    return nuevo

@router.get(
    "/", response_model=list[CategoriaRead]
)
async def listar_categorias(skip: int = 0, limit: int = 10):
    lista = listar(skip, limit)
    return lista

@router.get(
    "/{id}", response_model= CategoriaRead
)
async def detalle_categoria(id: int = Path(..., gt=0)) -> CategoriaRead:
    categoria = obtener_por_id(id)
    if categoria is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada.")
    return categoria

@router.put(
    "/{id}", response_model=CategoriaRead
)
async def actualizar_categoria(data: CategoriaCreate, id: int = Path(..., gt=0)):
    nuevo = actualizar_total(id, data)
    if nuevo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
    return nuevo

@router.put(
    "/{id}/desactivar", response_model=CategoriaRead
)
async def desactivar_categoria(id: int = Path(..., gt=0)):
    desactivado = desactivar(id)
    if desactivado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada.")
    return desactivado