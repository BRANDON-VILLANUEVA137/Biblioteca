#Pruebas de funcionalidad

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from crud import (
    crear_autor, obtener_autores, actualizar_autor, eliminar_autor,
    crear_libro, obtener_libros, actualizar_libro, eliminar_libro,
    crear_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario,
    buscar_libros_por_titulo, buscar_libros_por_genero, buscar_libros_por_autor
)

# Conexión y creación de la base de datos
engine = create_engine('sqlite:///biblioteca.db')  # Usa SQLite local
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#  PRUEBAS CRUD

# --- Autores ---
print("\n Insertando autores...")
crear_autor(session, "Gabriel García Márquez", "Colombiana")
crear_autor(session, "Isabel Allende", "Chilena")
for autor in obtener_autores(session):
    print(f"Autor: {autor.nombre} - {autor.nacionalidad}")

# --- Usuarios ---
print("\n Insertando usuarios...")
crear_usuario(session, "Carlos Pérez", "carlos@example.com", "3211234567")
crear_usuario(session, "Laura Gómez", "laura@example.com", "3007654321")
for usuario in obtener_usuarios(session):
    print(f"Usuario: {usuario.nombre} - {usuario.email}")

# --- Libros ---
print("\n Insertando libros...")
crear_libro(session, "Cien años de soledad", "Realismo mágico", 1967, 1)
crear_libro(session, "El amor en los tiempos del cólera", "Romance", 1985, 1)
crear_libro(session, "La casa de los espíritus", "Drama", 1982, 2)
for libro in obtener_libros(session):
    print(f"Libro: {libro.titulo} - {libro.genero} - {libro.año_publicacion}")

#  PRUEBAS BÚSQUEDAS

print("\n🔍 Búsqueda por título (parcial 'amor'):")
resultado = buscar_libros_por_titulo(session, "amor")
for libro in resultado:
    print(f"- {libro.titulo}")

print("\n🔍 Búsqueda por género ('drama'):")
resultado = buscar_libros_por_genero(session, "drama")
for libro in resultado:
    print(f"- {libro.titulo}")

print("\n🔍 Búsqueda por autor ('Gabriel'):")
resultado = buscar_libros_por_autor(session, "Gabriel")
for libro in resultado:
    print(f"- {libro.titulo}")

