from app.views.console_view import view,input_view
from app.models.db.actions import get_by_name
from app.controllers.game_controller import game
from app.modules.textos import *

def login(nombre,password):
    player = get_by_name(nombre)
    if player == None or player.password != password:
        view(NOT_LOGGED_IN)
        input_view(PRESS_ENTER)
    else:
        view(LOGGED_IN)
        game(player)