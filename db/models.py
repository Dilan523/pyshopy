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

    # Relación inversa: un rol tiene muchos usuarios
    usuarios = relationship("Usuario", back_populates="rol")

    
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
    # relación
    articulos = relationship("Articulo", back_populates="noticia")

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer,
                        primary_key=True)
    nombre_usuario = Column(String(60))
    apellido_usuario = Column(String(60))
    correo_usuario = Column(String(60))
    contrasena_usuario = Column(String(60))

    #clave foranea
    rol_id = Column(Integer, 
                    ForeignKey("roles.id_rol"))
    # Relación con SQLAlchemy para acceso sencillo
    rol = relationship("Rol", back_populates="usuarios")

class Articulo(Base):
    __tablename__ = "articulos"
    id_articulo = Column(Integer, primary_key=True)
    fecha_creacion = Column(Date)
    estado = Column(Boolean)
    nombre = Column(String(60))
    contenido = Column(String(200))
    #foranea
    noticia_id = Column(Integer, ForeignKey("noticias.id_noticia"))
    #relaciones
    noticia = relationship("Noticia", back_populates="articulos")
    comentarios = relationship("Comentario", back_populates="articulos")


class Comentario(Base):
    __tablename__ = "comentarios"
    id_comentario = Column(Integer, primary_key=True)
    fecha_creacion = Column(Date)
    contenido = Column(String(200))

    # Clave foránea
    articulo_id = Column(Integer, ForeignKey("articulos.id_articulo"))
    # Relación inversa
    articulo = relationship("Articulo", back_populates="comentarios")
