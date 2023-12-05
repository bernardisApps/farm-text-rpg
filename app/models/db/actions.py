from app.models.db.connection import create_session
from app.models.db.schemas import Player

def get_name(name):
    try:
        session = create_session()
        usuario = session.query(Player).filter_by(nombre=name).first()
        session.close()
        if usuario.nombre == name:
            return False
        else:
            return True
    except:
        return True

def get_user(name,password):
    try:
        session = create_session()
        user = session.query(Player).filter_by(nombre = name, password = password)
        session.close()
        return user
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