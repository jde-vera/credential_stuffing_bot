from pynput.keyboard import Controller, Key
from pynput import keyboard
import time
from exposed_logins import get_login

class KeyboardController:
    lst = get_login()
    index = 0

    @staticmethod
    def run_keyboard_controller():
        keyboard = Controller() 
        lst = KeyboardController.lst
        i = KeyboardController.index
        
        user = lst[i][1]
        password = lst[i][2]

        # iterate over the letters of the username
        for ch in range(len(user)):
            keyboard.press(user[ch])
            keyboard.release(user[ch])
        
        for ch in range(len(password)):
            keyboard.press(password[ch])
            keyboard.release(password[ch])

        lst.remove(lst[i])

        if len(KeyboardController.lst) == 0:
            return -1
        
        KeyboardController.run_keyboard_controller()


KeyboardController.run_keyboard_controller()
