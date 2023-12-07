from app.models.db.connection import create_session
from app.models.db.schemas import Player

def get_by_name(name):
    try:
        session = create_session()
        usuario = session.query(Player).filter_by(nombre=name).first()
        session.close()
        return usuario
    except:
        return False

def create_user(nombre,password,habilidad,recursos,construccion,fuerza,inteligencia,dinero,mochila,energia,lugar):
    try:
        session = create_session()
        p = Player(nombre,password,habilidad,recursos,construccion,fuerza,inteligencia,dinero,mochila,energia,lugar)
        session.add(p)    
        session.commit()
        session.close()
        return True
    except:
        return False
    
def save_user(nombre,habilidad,recursos,construccion,fuerza,inteligencia,dinero,mochila,energia,lugar):
    try:
        session = create_session()
        p = session.query(Player).filter_by(nombre = nombre).first()
        p.habilidad = habilidad
        p.recursos = recursos
        p.construccion = construccion
        p.fuerza = fuerza
        p.inteligencia = inteligencia
        p.dinero = dinero
        p.mochila = mochila
        p.energia = energia
        p.lugar = lugar
        session.commit()
        return True
    except:
        return False