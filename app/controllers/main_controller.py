from app.controllers.create_controller import creating_user
from app.controllers.login_controller import login
from app.views.console_view import view,input_view,limpiar
import sys
from app.modules.colorear import color
from app.modules.textos import *

def main():
    
    comando_valido = False
    
    while not comando_valido:
        limpiar()
        view(color('*'*len(WELCOME),'verdeclarito'))
        view(WELCOME)
        view(color('*'*len(WELCOME),'verdeclarito'))
        view(color(CREATED_BY,'rojo'))
        view('')
        view(MENU_OPTIONS)
        comandos = input_view('#> ').lower().split(' ')
        if len(comandos) < 1 or comandos[0] == '':
            view(INVALID_COMMAND)
            input_view(PRESS_ENTER)
        elif comandos[0] == 'registro':
            creating_user()
        elif comandos[0] == 'login':
            if len(comandos) == 3:
                nombre = comandos[1]
                password = comandos[2]
                login(nombre,password)
            else:
                view(INVALID_COMMAND)
                input_view(PRESS_ENTER)
        elif comandos[0] == 'salir':
            sys.exit()
        else:
            view(INVALID_COMMAND)
            input_view(PRESS_ENTER)
            