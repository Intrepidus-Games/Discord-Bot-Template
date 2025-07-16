

from colorama import Fore, Style
from enum import Enum
from lib.debug. import Logger

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

class Debug (Logger):
    def __init__(self, log_info:bool=True, log_warnings:bool=True, log_errors:bool=True):
        self.log_info = log_info
        self.log_warnings = log_warnings
        self.log_errors = log_errors
    
    def print(self, message:str, title:str="INFO"):
        if not self.log_info:
            return
        return self.log(message=message, title=title, title_color=Color.GREEN, title_enabled=True)
    
    def error(self, message:str, title:str="ERROR"):
        if not self.log_errors:
            return
        return self.log(message=message, title=title, title_color=Color.RED, title_enabled=True)
        
    def warn(self, message:str, title:str="WARNING"):
        if not self.log_warnings:
            return
        return self.log(message=message, title=title, title_color=Color.YELLOW, title_enabled=True)