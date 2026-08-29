from app.modules.producto.schemas import ProductoCreate, ProductoRead

db_productos = []
id_counter = 1

def crear(data: ProductoCreate) -> ProductoRead:
    global id_counter
    nuevo = ProductoRead(id=id_counter, **data.model_dump())
    db_productos.append(nuevo)
    id_counter += 1
    return nuevo

def listar(skip: int, limit: int) -> list[ProductoRead]:
    return db_productos[skip: skip+limit]

def obtener_por_id(id:int) -> ProductoRead | None:
    for producto in db_productos:
        if producto.id == id:
            return producto
    return None

def actualizar_total(data: ProductoCreate, id: int) -> ProductoRead | None:
    for producto in db_productos:
        if producto.id == id:
            nuevo = ProductoRead(id=id, **data.model_dump())
            db_productos.remove(producto)
            db_productos.append(nuevo)
            return nuevo
    return None

def desactivar(id: int) -> ProductoRead:
    for producto in db_productos:
        if producto.id == id:
            producto.activo = False
            return producto
    return None

def obtener_estado_stock(id: int) -> dict | None:
    producto = obtener_por_id(id)
    if producto is None:
        return None
    return {
        "stock": producto.stock,
        "bajo_stock_minimo": producto.stock < producto.stock_minimo,
        "activo": producto.activo
    }

     