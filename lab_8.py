from guizero import App, Slider,TextBox
from gpiozero import AngularServo
import time

Servo1 = 17  #3.3 pwr
Servo2 = 13 #3.3 pwr
minPulseWidth = (1/1000)
maxPulseWidth = (2/1000)

def slider_change1(slider_value):  #slider value for motor 1
    textbox.value = slider_value
    print(slider_value)
    servo1 = AngularServo(Servo1, min_pulse_width = minPulseWidth, max_pulse_width = maxPulseWidth, initial_angle = 0, min_angle = -0, max_angle = 90)
    servo1.angle = int(slider_value)
    
def slider_change2(slider_value):   #slider value for motor 2
    textbox.value = slider_value
    print(slider_value)
    servo2 = AngularServo(Servo2, min_pulse_width = minPulseWidth, max_pulse_width = maxPulseWidth, initial_angle = 0, min_angle = -0, max_angle = 90)
    servo2.angle = int(slider_value)

app = App()
slider1 = Slider(app, start=0, end=90, width="fill",command = slider_change)
slider2 = Slider(app, start=0, end=90, width="fill",command = slider_change2)
textbox = TextBox(app)
print(textbox.value)
app.display()