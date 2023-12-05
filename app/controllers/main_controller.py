from app.controllers.create_controller import creating_user
from app.views.console_view import view,input_view
import os
import sys
from app.modules.colorear import color

def main():
    os.system('cls')
    view('**************************')
    view('Bienvenido a Farm-Text-Rpg')
    view('**************************')
    view('')
    view(f'Si tienes un usuario ingresa {color("<login> <nombre> <password>","cian")} pero sin las <>.')
    view(f'Sino ingresa {color("<registro>","cian")} también sin las <>')
    view('También puede escribir salir para quitar el juego.')
    comando_valido = False
    while not comando_valido:
        comandos = input_view('#> ').split(' ')
        if len(comandos) < 1 or comandos[0] == '':
            view('Error en el comando. Intente nuevamente.')
            input_view('Presione una tecla para continuar...')
        elif comandos[0] == 'registro':
            creating_user()
            comando_valido = True
        elif comandos[0] == 'login':
            if len(comandos) == 3:
                nombre = comandos[1]
                password = comandos[2]
            else:
                view('Comando inválido. Intente nuevamente.')
                input_view('Presione una tecla para continuar...')
        elif comandos[0] == 'salir':
            sys.exit()
            