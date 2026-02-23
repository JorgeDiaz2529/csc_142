# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds,  etc.
header = pygwidgets.DisplayText(window, (10, 25), 'GUI Temperature Converter', 
                                    fontSize=36, textColor=WHITE)

temperatureInput = pygwidgets.InputText(window, (10, 55), "",
                                    fontSize=24, textColor=BLACK, backgroundColor=WHITE,)

farenheit_converter = pygwidgets.TextRadioButton(window, (10, 100), "RadioButtonGroup", "Farenheit",
                                                 fontSize=30, textColorDeselected=WHITE, circleColorDeselected=GRAY,
                                                 textColorSelected=GRAY, circleColorSelected=GRAY)

celsius_converter = pygwidgets.TextRadioButton(window, (10, 140), "RadioButtonGroup", "Celsius",
                                                 fontSize=30, textColorDeselected=WHITE, circleColorDeselected=GRAY,
                                                 textColorSelected=GRAY, circleColorSelected=GRAY)

output = pygwidgets.DisplayText(window, (10, 200), 'Result:', 
                                    fontSize=40, textColor=WHITE)


# temperature conversion functions
def convert_to_farenheit(temp: int):
     return temp * 9/5 + 32

def convert_to_celsius(temp: int):
     return (temp - 32) / (9/5)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if temperatureInput.handleEvent(event):
            pass

        if farenheit_converter.handleEvent(event):
            temperature = temperatureInput.getValue()

            try:
                result = convert_to_farenheit(int(temperature))
                output.setValue(f"Result: {result:.0f} F°")
            except ValueError:
                print("Not a valid number.")                
                
        if celsius_converter.handleEvent(event):
            temperature = temperatureInput.getValue()

            try:
                result = convert_to_celsius(int(temperature))
                output.setValue(f"Result: {result:.0f} C°")
            except ValueError:
                print("Not a valid number.")  


    # 8 - Do any "per frame" actions
    window.fill(BLACK) # AAAAAAAAAAAA

    header.draw()
    temperatureInput.draw()

    farenheit_converter.draw()
    celsius_converter.draw()

    output.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait