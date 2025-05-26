from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#connection string
#represenat la base de datos a conectar 
#dependiendo la base de datos que se use y el lenguaje de programación
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3315/sn-52_3147234'

#crea el objeto de conexion(permite conectarse a la base de datos)
conn = create_engine(SQLALCHEMY_DATABASE_URL)

#la clase base para los modelos de la base de datos
Base = declarative_base()