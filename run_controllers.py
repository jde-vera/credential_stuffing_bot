import threading
from mouse_monitor import run_mouse_controller
from keyboard_controller import KeyboardController

if __name__ == '__main__':
    thread1 = threading.Thread(target=run_mouse_controller)
    thread2 = threading.Thread(target=KeyboardController.run_keyboard_controller)

    thread1.start()
    thread2.start()