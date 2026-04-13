#Card class
import pygame
import pygwidgets

class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.cardName = rank + " of " + suit
        fileName = "images/" + self.cardName + ".png"
        #starting location
        self.images = pygwidgets.ImageCollection(window, (0,0),
                                                 {'front': fileName, 'back': Card.BACK_OF_CARD_IMAGE},
                                                 'back')
        
    def conceal(self):
        self.images.replace('back')
    
    def reveal(self):
        self.images.replace('front')
    
    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank

    def setLoc(self, loc): #calls image collection's setloc method
        self.images.setLoc(loc)