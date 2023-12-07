from app.views.console_view import view, input_view
from app.modules.colorear import color
import json

class Jugador():
    def __init__(self) -> None:
        self.nombre = ""
        self.password = ""
        self.habilidad = 0
        self.recursos = 0
        self.construccion = 0
        self.fuerza = 0
        self.inteligencia =0
        self.dinero = 0
        self.mochila = []
        self.energia = 0
        self.lugar = ""

def game(jugador):
    j = Jugador()
    for key in vars(jugador):
        if key == 'mochila':
            mochila_str = getattr(jugador,key)
            mochila = json.loads(mochila_str)
            setattr(j,key,mochila)
        else:
            setattr(j, key, getattr(jugador, key))
    
    view(f'Bienvenido {j.nombre}')
    input_view()