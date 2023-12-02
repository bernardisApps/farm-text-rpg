from app.controllers.create_controller import creating_user
from app.views.console_view import view,input_view

def main():
    view('**************************')
    view('Bienvenido a Farm-Text-Rpg')
    view('**************************')
    view('')
    view('Si tienes un usuario ingresa <login> <nombre> <password> pero sin las <>.')
    view('Sino ingresa <registro> también sin las <>')
    input_view()