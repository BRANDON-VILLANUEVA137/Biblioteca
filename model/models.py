from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    libros = relationship('Libro', back_populates='autor')

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    genero = Column(String)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = relationship('Autor', back_populates='libros')
    prestamos = relationship('Prestamo', back_populates='libro')


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    prestamos = relationship('Prestamo', back_populates='usuario')

