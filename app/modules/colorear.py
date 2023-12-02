from colorama import Fore, Style

def color(string, color):
    if color == 'rojo':
        color = Fore.RED
    elif color == 'verde':
        color = Fore.GREEN
    elif color == 'azul':
        color = Fore.BLUE
    elif color == 'verdeclarito':
        color = Fore.LIGHTGREEN_EX
    elif color == 'cian':
        color = Fore.LIGHTCYAN_EX
    elif color == 'amarillo':
        color = Fore.YELLOW
    return color+string+Style.RESET_ALL