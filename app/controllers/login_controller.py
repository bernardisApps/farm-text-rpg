from app.views.console_view import view,input_view
from app.models.db.actions import get_by_name
from app.controllers.game_controller import game

def login(nombre,password):
    player = get_by_name(nombre)
    if player == None or player.password != password:
        view('Usuario incorrecto. Intenta nuevamente.')
        input_view('Presione una tecla para continuar...')
    else:
        view('Logueado correctamente.')
        game(player)