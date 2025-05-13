from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from crud import *
from prestamos import *
from consultas import *
from datetime import date

# Configuración de la base de datos
engine = create_engine('sqlite:///biblioteca.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def menu():
    while True:
        print("\n📚 SISTEMA DE BIBLIOTECA")
        print("1. Crear autor")
        print("2. Crear libro")
        print("3. Crear usuario")
        print("4. Buscar libro")
        print("5. Registrar préstamo")
        print("6. Devolver libro")
        print("7. Ver préstamos activos")
        print("8. Autor con más libros")
        print("9. Usuarios con préstamos vencidos")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del autor: ")
            crear_autor(session, nombre)

        elif opcion == "2":
            titulo = input("Título del libro: ")
            genero = input("Género: ")
            autor_id = int(input("ID del autor: "))
            crear_libro(session, titulo, genero, autor_id)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            crear_usuario(session, nombre)

        elif opcion == "4":
            print("Buscar por: 1. Título | 2. Género | 3. Autor ID")
            tipo = input("Opción: ")
            if tipo == "1":
                texto = input("Título (parcial): ")
                libros = buscar_libro_por_titulo(session, texto)
            elif tipo == "2":
                genero = input("Género: ")
                libros = buscar_libro_por_genero(session, genero)
            elif tipo == "3":
                autor_id = int(input("ID del autor: "))
                libros = buscar_libro_por_autor(session, autor_id)
            else:
                libros = []
            for libro in libros:
                print(f"{libro.id}: {libro.titulo} - {libro.genero}")

        elif opcion == "5":
            libro_id = int(input("ID del libro: "))
            usuario_id = int(input("ID del usuario: "))
            registrar_prestamo(session, libro_id, usuario_id, date.today())

        elif opcion == "6":
            prestamo_id = int(input("ID del préstamo: "))
            devolver_libro(session, prestamo_id, date.today())

        elif opcion == "7":
            prestamos = listar_prestamos_activos(session)
            for p in prestamos:
                print(f"ID: {p.id} | Libro: {p.libro.titulo} | Usuario: {p.usuario.nombre}")

        elif opcion == "8":
            resultado = autor_con_mas_libros(session)
            print(f"Autor con más libros: {resultado[0]} ({resultado[1]} libros)")

        elif opcion == "9":
            usuarios = usuarios_con_prestamos_vencidos(session)
            for u in usuarios:
                print(f"Usuario: {u.nombre}")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
