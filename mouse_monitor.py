from pynput.mouse import Controller
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

mouse = Controller()
mouse.position = (231,100)
time.sleep(5)
mouse.move(0,35)
time.sleep(5)
mouse.move(0,37)
time.sleep(5)
mouse.move(-196,37)