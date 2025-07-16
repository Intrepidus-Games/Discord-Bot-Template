from colorama import Fore, Style
from enum import Enum

class Color(Enum):
    BLACK           = Fore.BLACK 
    RED             = Fore.RED   
    GREEN           = Fore.GREEN 
    YELLOW          = Fore.YELLOW
    BLUE            = Fore.BLUE  
    MAGENTA         = Fore.MAGENTA
    CYAN            = Fore.CYAN  
    WHITE           = Fore.WHITE 
    RESET           = Fore.RESET 
    LIGHTBLACK_EX   = Fore.LIGHTBLACK_EX  
    LIGHTRED_EX     = Fore.LIGHTRED_EX    
    LIGHTGREEN_EX   = Fore.LIGHTGREEN_EX  
    LIGHTYELLOW_EX  = Fore.LIGHTYELLOW_EX 
    LIGHTBLUE_EX    = Fore.LIGHTBLUE_EX   
    LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
    LIGHTCYAN_EX    = Fore.LIGHTCYAN_EX   
    LIGHTWHITE_EX   = Fore.LIGHTWHITE_EX  

class Logger:
    def __init__(self):
        pass

    def colored_message(self, message: str, color:Color=Color.WHITE) -> str:
        return f"{color.value}{message}"

    def log(self, message:str, title:str="INFO", title_color:Color=Color.GREEN)->None:
        print(f"{title_color.value}{title}{Fore.WHITE}:     {message} {Style.RESET_ALL}")