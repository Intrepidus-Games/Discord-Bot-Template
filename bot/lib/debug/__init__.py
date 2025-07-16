

from colorama import Fore, Style
from enum import Enum
from lib.debug.logger import Logger, Color

class Debug (Logger):
    def __init__(self, log_info:bool=True, log_warnings:bool=True, log_errors:bool=True):
        self.log_info = log_info
        self.log_warnings = log_warnings
        self.log_errors = log_errors
    
    def print(self, message:str, title:str="INFO"):
        if not self.log_info:
            return
        return self.log(message=message, title=title, title_color=Color.GREEN)
    
    def error(self, message:str, title:str="ERROR"):
        if not self.log_errors:
            return
        return self.log(message=message, title=title, title_color=Color.RED)
        
    def warn(self, message:str, title:str="WARNING"):
        if not self.log_warnings:
            return
        return self.log(message=message, title=title, title_color=Color.YELLOW)