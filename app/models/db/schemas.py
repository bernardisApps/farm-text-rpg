from typing import Any
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = 'players'
    nombre = Column(String(10),primary_key=True)
    password = Column(String(15))
    habilidad = Column(Integer)
    recursos = Column(Integer)
    construccion = Column(Integer)
    fuerza = Column(Integer)
    inteligencia = Column(Integer)
    dinero = Column(Float)
    mochila = Column(String)
    energia = Column(Integer)
    lugar = Column(String)
    
    def __init__(self, nombre, password,habilidad,recursos,construccion,fuerza,inteligencia,dinero,mochila,energia,lugar):
        super().__init__()
        self.nombre = nombre
        self.password = password
        self.habilidad = habilidad
        self.recursos = recursos
        self.construccion = construccion
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.dinero = dinero
        self.mochila = mochila
        self.energia = energia
        self.lugar = lugar