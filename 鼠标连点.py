from pymouse import PyMouse
from pynput import keyboard
import time
m=PyMouse()
break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
    elif key == keyboard.Key.space:
        print ('start pressed')
        break_program = False   
 ####        return False
for i in range(4):

    print(i)

    time.sleep(1)
        
with keyboard.Listener(on_press=on_press) as listener:

    while True:

            while break_program == False:
                m.click(m.position()[0],m.position()[1],1)
                time.sleep(0.05)

    listener.join
