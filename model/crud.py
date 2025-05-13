#Funciones CRUD y búsquedas
from models import Autor,Libro,Usuario


#siAutor Crud
#Crear
def crear_autor(session, nombre, nacionalidad):
    autor = Autor(nombre=nombre, nacionalidad=nacionalidad)
    session.add(autor)
    session.commit()

#Consultar
def obtener_autores(session):
    return session.query(Autor).all()

#Actualizar
def actualizar_autor(session, autor_id, nuevos_datos):
    autor = session.query(Autor).get(autor_id)
    if autor:
        for k, v in nuevos_datos.items():
            setattr(autor, k, v)
        session.commit()

#Eliminar
def eliminar_autor(session, autor_id):
    autor = session.query(Autor).get(autor_id)
    if autor:
        session.delete(autor)
        session.commit()


#Libro Crud
#Crear
def crear_libro(session, titulo, genero, año_publicacion, autor_id):
    libro = Libro(titulo=titulo, genero=genero, año_publicacion=año_publicacion, autor_id=autor_id)
    session.add(libro)
    session.commit()
    
#Consultar
def obtener_libros(session):
    return session.query(Libro).all()

#Actualizar
def actualizar_libro(session, libro_id, nuevos_datos):
    libro = session.query(Libro).get(libro_id)
    if libro:
        for k, v in nuevos_datos.items():
            setattr(libro, k, v)
        session.commit()

#Eliminar
def eliminar_libro(session, libro_id):
    libro = session.query(Libro).get(libro_id)
    if libro:
        session.delete(libro)
        session.commit()


#Usuario Crud
#Crear
def crear_usuario(session, nombre, email, telefono):
    usuario = Usuario(nombre=nombre, email=email, telefono=telefono)
    session.add(usuario)
    session.commit()

#Consultar
def obtener_usuarios(session):
    return session.query(Usuario).all()

#Actualizar
def actualizar_usuario(session, usuario_id, nuevos_datos):
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        for k, v in nuevos_datos.items():
            setattr(usuario, k, v)
        session.commit()

#Eliminar
def eliminar_usuario(session, usuario_id):
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        session.delete(usuario)
        session.commit()


#Funciones buscar libro

#Por titulo
def buscar_libros_por_titulo(session, texto):
    return session.query(Libro).filter(Libro.titulo.ilike(f"%{texto}%")).all()

#Por genero
def buscar_libros_por_genero(session, genero):
    return session.query(Libro).filter(Libro.genero.ilike(f"%{genero}%")).all()

#Por autor
def buscar_libros_por_autor(session, nombre_autor):
    return session.query(Libro).join(Autor).filter(Autor.nombre.ilike(f"%{nombre_autor}%")).all()

