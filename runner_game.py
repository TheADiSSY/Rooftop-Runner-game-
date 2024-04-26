#Placeholder name for running game
import pygame, sys, gif_pygame
import random
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage, Tk


#Name, background and CLOCK
pygame.display.set_caption("Rooftop Run")

Screen_Height = 1080
Screen_Width = 1920
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

score = 0


pygame.init()
clock = pygame.time.Clock()


#Hand drawn assets
Floor = gif_pygame.load("Runner Game/floor/amazing floor.gif")
Background = pygame.image.load('Runner Game/runner bg.png')
Vent = pygame.image.load('Runner Game/vent.png')
Vent_spawn = False

#Player
Player = "run"
Player_x = 270
Player_y = 340
Run_animation = gif_pygame.load("Runner Game/Player Character/run animation coloured.gif") 
gif_pygame.transform.scale(Run_animation, (700, 700))
Jump_animation = gif_pygame.load("Runner Game/Player Character/jump animation coloured with smear.gif")
gif_pygame.transform.scale(Jump_animation, (700, 700))

#asset coordinates
vent_x = 1910
vent_y = 750


#The gameloop
running = True
while running:


    #Loading the scenery
    Screen.blit(Background,(0,0))
    Floor.render(Background, (0,800))

    #Player
    if Player == "run":
        Run_animation.render(Background, (Player_x, Player_y))
        pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        Player = "jump"
    
    if Player == "jump":
        Jump_animation.render(Background, (Player_x, Player_y))
        
        Player = "run"
    #Obstacles
    Obstacle_chance = random.randint(1,20)
    if Obstacle_chance == 5:
        Vent_spawn = True

    if Vent_spawn == True:
        Background.blit(Vent,(vent_x,vent_y))

    
    #Closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Score display
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (85, 0, 102))
    Screen.blit(score_text, (500, 250))


    score = score + 1


    # Update the display
    pygame.display.flip()
    clock.tick(50)

print("You scored", score, "points")

if score >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    print("Please, just go outside. There's better things you can do with your life...")
elif score >= 1000000000000000000000000000000:
    print("If you get to the last milestone, I'll share you a secret to life.")
elif score >= 1000000:
    print("Wow, scoring", score, "points? You truly have no limits, master!!")
elif score >= 500000:
    print(score, "points? Are we pushing for a million or something?! That's an insanely good score!!!")
elif score >= 300000:
    print("You cheating or something? This score is insane")
elif score >= 225000:
    print("You're reaching pretty far! Keep it up!")
elif score >= 150000:
    print("You're super dedicated, ain't ya?!")
elif score >= 100000:
    print("Incredible!! How are you this good??!!")
elif score >= 70000:
    print("NOW THAT'S A GIGANTIC SCORING!!!")
elif score == 69420:
    print("Wow, I bet you think you're reeeeeaaaally funny, don't you?")
elif score >= 50000:
    print("My goodness, you're doing awesome!!!!!")
elif score == 42069:
    print("Haha, that's kinda funny. I hope that's a coincidence. If not, get out.")
elif score >= 30000:
    print("TIRTY TOUSAND AND MORE!!!!!!!????? That's like, ten tousand... TIMES TREE!! You're extremely good at this!!!!!")
elif score >= 15000:
    print("Yeah, yeah!!! You're a prodigy, my friend!!")
elif score >= 10000:
    print("You endured running this long?! AMAZING!!")
elif score >= 5000:
    print("Woah, you lasted that long??!! You're doing great at this!!")  
elif score >= 1500:
    print("Hmmm... That's what we call a pretty neat score!")  
elif score >= 500:
    print("Yeah, you're getting the hang of it! Nice!")
elif score <= 100:
    print("Wow, it's kinda impressive how fast you lost...")
elif score <= 499:
    print("Hmmmm.... you're definetely going somewhere.")