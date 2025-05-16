from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship


class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer,
                primary_key=True)
    fecha_creacion = Column(Date)
    estado = Column(Boolean)
    nombre = Column(String(60))
    
    #relacion uno a muchos

    noticias = relationship("Noticia", 
                       back_populates="categoria")
    
class Rol(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer,
                primary_key=True)
    fecha_creacion = Column(Date)
    nombre = Column(String(60))
    

    
class Noticia(Base):
    __tablename__ = "noticias"
    id_noticia = Column(Integer,
                primary_key=True)
    fecha_creacion = Column(Date)
    estado = Column(Boolean)
    nombre = Column(String(60))
    descripcion = Column(String(200))
    
    #clave foranea
    categoria_id = Column(Integer, 
                          ForeignKey("categorias.id_categoria"))
