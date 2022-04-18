import time
from plyer import notification
from pynotifier import Notification
from pynput import keyboard

# Global variable to update when User presses the desired key
break_program = False   # Set to FALSE (Default)

# Function run on Key press
def on_press(key):
    global break_program
    print (key)

    # Check if User has pressed the 'end' key or not
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True    # Change to TRUE
        return False            # Return FALSE

# Keep the program Live until User presses the desired Key
with keyboard.Listener(on_press=on_press) as listener:

    # Will run only when global variable is set to False
    while break_program == False:

        # YOUR CODE GOES HERE #
        
        Notification(
	title='POMODORO ACTIVITY',
	description='Assalam o alikum : kindly take 5 to 10 minutes rest you are countinous working since more then 25 minutes',
	icon_path='icon.ico', 
	duration=20,                                   
	urgency='normal'
).send()
        print ('program running')
        time.sleep(25*60)
    listener.join()




