from app.models.db.actions import create_user,get_by_name
from app.views.console_view import view,input_view,input_pass,limpiar
import json
import time
from app.modules.textos import *

def creating_user():
    view(WELCOME_NEW_USER)
    nombre = ''
    correcto = False
    while not correcto:
        nombre = input_view('#> ').lower()
        if nombre == '' or len(nombre) > 10:
            view(INVALID_NAME)
            input_view(PRESS_ENTER)
        else:
            esta_disponible = get_by_name(nombre) == None
            if esta_disponible:
                view(CORRECT_NAME)
                correcto = True
            else:
                view(USED_NAME)
                
    password = ''
    view(PASSWORD_CHOOSE)
    while password == '':
        password = input_pass('#> ').lower()
        if password != "":
            view(VERY_GOOD)
            view(CREATING_CHARACTER)
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
                view(CREATED_CHARACTER)
                input_view(PRESS_ENTER)
                limpiar()
            