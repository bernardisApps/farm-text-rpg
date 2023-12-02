from app.models.db.actions import create_user
from app.views.console_view import view,input_view
from app.modules.colorear import color

def creating_user():
    msj = 'Bienvenido nuevo usuario. Vamos a crear tu personaje.'
    msj2 = 'Primero necesitamos que elijas un nombre.'
    msj3 = 'El mismo debe ser menor a 10 carácteres y no debe ser nulo.'
    view(msj)
    view(msj2)
    view(msj3)
    nombre = ''
    while nombre == '' or len(nombre) > 10:
        nombre = input_view('#> ')
        if nombre == '' or len(nombre) > 10:
            view('El nombre no es válido, intenta nuevamente.')
            input_view('Presione una tecla para continuar...')
        else:
            view('Muy bien!')
            view()
    password = ''
    msj4 = 'Ahora debes elegir un password.'
    view(msj4)
    while password == '':
        password = input_view('#> ')
        if password != "":
            view('Excelente!.')
            input_view('Presione una tecla para continuar...')