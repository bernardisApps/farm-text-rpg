from app.models.db.actions import create_user,get_name
from app.views.console_view import view,input_view,input_pass,limpiar
import json
import time

def creating_user():
    msj = 'Bienvenido nuevo usuario. Vamos a crear tu personaje.'
    msj2 = 'Primero necesitamos que elijas un nombre.'
    msj3 = 'El mismo debe ser menor a 10 carácteres y no debe ser nulo.'
    view(msj)
    view(msj2)
    view(msj3)
    nombre = ''
    correcto = False
    while not correcto:
        nombre = input_view('#> ').lower()
        if nombre == '' or len(nombre) > 10:
            view('El nombre no es válido, intenta nuevamente.')
            input_view('Presione una tecla para continuar...')
        else:
            esta_disponible = get_name(nombre)
            if esta_disponible:
                view('Muy bien! el nombre está disponible.')
                correcto = True
            else:
                view('El nombre ya está en uso, por favor elije otro nombre: ')
                
    password = ''
    msj4 = 'Ahora debes elegir un password.'
    view(msj4)
    while password == '':
        password = input_pass('#> ').lower()
        if password != "":
            view('Excelente!.')
            view('Creando personaje...')
            time.sleep(1)
            se_creo = create_user(nombre,
                        password,
                        1,
                        1,
                        1,
                        1,
                        1,
                        100,
                        json.dumps([]),
                        10,
                        'habitacion')
            if se_creo:
                view('Personaje creado correctamente.')
                input_view('Presione una tecla para continuar...')
                limpiar()
            