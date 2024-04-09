#Placeholder name for running game
import pygame
import time
import random
import cv2
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage, Tk


#Name, background and CLOCK
pygame.display.set_caption("Rooftop Run")

Screen_Height = 1080
Screen_Width = 1920
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

pygame.init()
background = 'C:/Desktop/Runner Game/runner bg.png'
clock = pygame.time.Clock()

#The gameloop
running = True
while running:
    #The game's background
    Screen.blit(background, (0, 0))
    
    # Update the display
    pygame.display.flip()

    #Closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False