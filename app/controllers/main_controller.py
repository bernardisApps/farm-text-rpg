from app.controllers.create_controller import creating_user
from app.views.console_view import view,input_view

def main():
    view('**************************')
    view('Bienvenido a Farm-Text-Rpg')
    view('**************************')
    view('')
    view('Si tienes un usuario ingresa <login> <nombre> <password> pero sin las <>.')
    view('Sino ingresa <registro> también sin las <>')
    comando = input_view('#> ')
    if comando.split()[0] == 'registro':
        creating_user()