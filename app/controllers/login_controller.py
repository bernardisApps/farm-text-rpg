from app.views.console_view import view,input_view,input_pass,limpiar
from app.models.db.actions import get_user

def login(nombre,password):
    player = get_user(name=nombre,password=password)
    return player
