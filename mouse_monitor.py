from pynput.mouse import Controller, Button
from pynput import mouse 
import time
def on_move(x,y):
    print(f'pointer moved (x={x}, y={y})')
def on_click(x,y,button,pressed):
    if not pressed:
        return False
    
# with mouse.Listener(on_move=on_move,on_click=on_click) as listener:
#     listener.join()

# co-ords
# username = (x=231,y=100)
# password = (x=231,y=135)
# confirm_password = (x=231,y=172)
# login = (x=35,y=209)

def run_mouse_controller():
    while True:
        mouse = Controller()
        mouse.position = (231,100) # this is the co-ords of the username
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(10)

        mouse.move(249,26) # this is to close the saved info 
        mouse.press(Button.left)
        mouse.release(Button.left)
        
        time.sleep(5)

        mouse.move(-249,9) # this is the co-ords of the password
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(15)

        mouse.move(0,37)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(15)

        mouse.move(-196,37)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(1)