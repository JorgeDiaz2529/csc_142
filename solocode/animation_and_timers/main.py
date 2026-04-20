import pygame
import pygwidgets
import sys
import math

WIDTH = 500
HEIGHT = 550

class Stopwatch():
    def __init__(self):
        pygame.init()

        #pygame variables
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        #time variables
        self.startTime = 0
        self.timeElapsed = 0
        self.stopwatchEnabled = False

        pygame.display.set_caption("Stopwatch")


    def run(self):
        start_button = pygwidgets.TextButton(self.screen, (0,0), "Start")
        stop_button = pygwidgets.TextButton(self.screen, (0,0), "Stop")
        time_text = pygwidgets.DisplayText(self.screen, 
                                           (0,0), 
                                           "0.00", 
                                           textColor=(255,255,255),
                                           fontSize=32)
        
        header = pygwidgets.DisplayText(self.screen, 
                                        (0,0), 
                                        "THE TIMER", 
                                           textColor=(255,255,255),
                                           fontSize=48)
        
        start_button.setCenteredLoc((WIDTH/2, 400))
        stop_button.setCenteredLoc((WIDTH/2, 460))
        time_text.setCenteredLoc((WIDTH/2, 320))
        header.setCenteredLoc((WIDTH/2, 50))

        #for the circlePos and math stuff
        circleX, circleY = WIDTH/2, 180,
        length = 80


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #pygwidget events
                if start_button.handleEvent(event):
                    self.stopwatchEnabled = True
                    self.startTime = pygame.time.get_ticks() # Resets the timer

                if stop_button.handleEvent(event):
                    self.stopwatchEnabled = False
            

            self.screen.fill((0,0,0))

            #LOGIC
            if self.stopwatchEnabled == True:
                self.timeElapsed = pygame.time.get_ticks() - self.startTime
                time_text.setValue(f"{self.timeElapsed/1000:.2f}")

                #P.S. had to look up a lot of the mathematical stuff here
                angle = (self.timeElapsed / math.pi) % 360 # close enough I guess??

                radians = math.radians(angle - 90)
                
                endX = circleX + length * math.cos(radians)
                endY = circleY + length * math.sin(radians)

                pygame.draw.line(self.screen, (255,150,150), (circleX, circleY), (endX, endY), 4)


            #DISPLAY

            pygame.draw.circle(self.screen, (255,255,255),(circleX, circleY),80,4)

            start_button.draw()
            stop_button.draw()
            time_text.draw()
            header.draw()

            pygame.display.flip()

            self.clock.tick(60)
        


if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.run()