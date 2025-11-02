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

        time.sleep(1)

        # iterate over the letters of the username
        for ch in range(len(user)):
            keyboard.press(user[ch])
            keyboard.release(user[ch])
            time.sleep(1)
        
        time.sleep(10)
        
        for ch in range(len(password)):
            keyboard.press(password[ch])
            keyboard.release(password[ch])
            time.sleep(1)

        time.sleep(3)
        
        for ch in range(len(password)):
            keyboard.press(password[ch])
            keyboard.release(password[ch])
            time.sleep(1)
        
        time.sleep(3)
        
        lst.remove(lst[i])

        if len(KeyboardController.lst) == 0:
            return -1
        
        KeyboardController.run_keyboard_controller()