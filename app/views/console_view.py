from getpass import getpass
import os

def view(texto:str = ''):
    print(texto)
    
def input_view(texto:str=''):
    return input(texto)

def input_pass(texto:str=''):
    return getpass(texto)

def limpiar():
    os.system('cls')