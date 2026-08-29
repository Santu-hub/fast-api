from app.modules.categoria.schemas import CategoriaCreate, CategoriaRead

db_categorias: list[CategoriaRead] = [
    CategoriaRead(id=1, codigo="MUE-01", descripcion="Muebles de Oficina", activo=True),
    CategoriaRead(id=2, codigo="ELE-02", descripcion="Electrónica", activo=True),
]
id_counter = 3

def crear(data: CategoriaCreate) -> CategoriaRead:
    global id_counter
    categoria_nueva = CategoriaRead(id=id_counter, **data.model_dump())
    db_categorias.append(categoria_nueva)
    id_counter += 1
    return categoria_nueva

def listar(skip: int, limit: int) -> list[CategoriaRead]:
    return db_categorias[skip: skip+limit]

def obtener_por_id(id: int) -> CategoriaRead | None:
    for categoria in db_categorias:
        if categoria.id == id:
            return categoria
    return None

def actualizar_total(id: int, data: CategoriaCreate) -> CategoriaRead | None:
    for categoria in db_categorias:
        if categoria.id == id:
            nueva = CategoriaRead(id=id, **data.model_dump())
            db_categorias.remove(categoria)
            db_categorias.append(nueva)
            return nueva
    return None

def desactivar(id:int) -> CategoriaRead | None:
    for categoria in db_categorias:
        if categoria.id == id:
            categoria.activo = False
            return categoria
    return None