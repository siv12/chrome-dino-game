# programmer -> siv
# chrome dino game

import pygame            # importing essential modules
import random
import math
x = pygame.init()       
pygame.mixer.init()       # initialising pygame

width = 600              
height = 360

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))   # creating game window
pygame.display.set_caption('Dino')                  # setting caption of game 
background = pygame.image.load('sprites/background.png')     # importing background 

# importing character 
dino1 = pygame.image.load('sprites/dra1.png').convert_alpha()   
dino1 = pygame.transform.scale(dino1, (60, 60))             # scaling 

dino2 = pygame.image.load('sprites/dra2.png').convert_alpha()
dino2 = pygame.transform.scale(dino2, (60, 60))

dino3 = pygame.image.load('sprites/dra3.png').convert_alpha()
dino3 = pygame.transform.scale(dino3, (60, 60))

dino4 = pygame.image.load('sprites/dra4.png').convert_alpha()
dino4 = pygame.transform.scale(dino4, (60, 60))

# importing dock pose of character
dock1 = pygame.image.load('sprites/dock1.png').convert_alpha()
dock1 = pygame.transform.scale(dock1, (60, 40))

dock2 = pygame.image.load('sprites/dock2.png').convert_alpha()
dock2 = pygame.transform.scale(dock2, (60, 40))

# importing obstacles
tree1 = pygame.image.load('sprites/tree1.png').convert_alpha()
tree1 = pygame.transform.scale(tree1, (65, 65))

tree2 = pygame.image.load('sprites/tree2.png').convert_alpha()
tree2 = pygame.transform.scale(tree2, (75, 55))

tree3 = pygame.image.load('sprites/tree3.png').convert_alpha()
tree3 = pygame.transform.scale(tree3, (90, 60))

tree4 = pygame.image.load('sprites/tree4.png').convert_alpha()
tree4 = pygame.transform.scale(tree4, (30, 60))

tree5 = pygame.image.load('sprites/tree5.png').convert_alpha()

bird1 = pygame.image.load('sprites/bird1.png').convert_alpha()
bird1 = pygame.transform.scale(bird1, (70, 70))

bird2 = pygame.image.load('sprites/bird2.png').convert_alpha()
bird2 = pygame.transform.scale(bird2, (60, 60))

# lists to perform walk , dock , bird wings flap animation
walk = [dino2, dino2, dino2, dino3, dino3, dino3]
dock = [dock1, dock1, dock1, dock2, dock2, dock2]
bird = [bird1, bird1, bird1, bird2, bird2, bird2]

font=pygame.font.SysFont(None,35)     # font

def welcome():        # welcome screen function
    exitgame = False
    while not exitgame:
        start = pygame.image.load('sprites/start.png').convert_alpha()
        start = pygame.transform.scale(start, (600, 357))
        screen.blit(start, (0, 0))          # blitting the welcome page on the screen 

        # handling keyboard events
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound=pygame.mixer.Sound('sounds/jump.mp3')
                    sound.play()
                    gameloop()     # calling gameloop function
        pygame.display.update()         # updating the screen

def gameloop():       # making gameloop function
    # initialising variables with boolean values
    exitgame = False
    gameover = False
    jump = False
    jump_control = True
    walkpoint = 0
    dockpoint = 0
    birdpoint = 0
    bird_2_point = 0
    walk_control = True
    dock_control = False
    bird_control = False
    bird2_control = False
    background_control = True
    tree_control = True
    bird_move_control=True
    playsound=True
    playsound_1=True
    score=0
    i = 100

    fps = 30   # frame per second

    # handling the sprites location on the screen
    background_x = 0
    background_y = 0
    background_change=7

    dino1_x = 30
    dino1_y = 282
    dino_y_vel = 10

    dock_x = 30
    dock_y = 300

    tree1_x = 570
    tree1_y = 275
    tree1_x_change = 7

    tree2_x = 1200
    tree2_y = 279
    tree2_x_change = 7

    tree3_x = 1700
    tree3_y = 275
    tree3_x_change = 7

    tree4_x = 2200
    tree4_y = 276
    tree4_x_change = 7

    tree5_x = 2900
    tree5_y = 272
    tree5_x_change = 7

    bird1_x = 1900
    bird1_y = 243
    bird2_x = 7000
    bird2_y = 275
    bird1_x_change = 9
    bird2_x_change = 9

    # function for handling collisions with the obstacles
    def iscollision(dino_x, dino_y, obs_x, obs_y):
        distance = math.sqrt(math.pow(dino_x-obs_x, 2) + math.pow(dino_y-obs_y, 2))
        if distance < 40:
            return True
        else:
            return False

    # function for handling text on the screen
    def text_screen(text,colour,x,y):
        screen_text=font.render(text,True,colour)  # a pygame function "render()"
        screen.blit(screen_text,[x,y])
    
    # opening hiscore file to store our hiscore values
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
    
    # Game loop 
    while not exitgame:
        # moving our background horizontally and again blitting it after the first image ends
        if background_control == True:
            s = background_x % background.get_rect().width
            screen.blit( background, (s-background.get_rect().width, background_y))
            if background_x < width:
                screen.blit(background, (s, background_y))
            background_x -= background_change
            score+=1     # increasing scores
                               
        # blitting sprites on screen 
        screen.blit(tree1, (tree1_x, tree1_y))
        screen.blit(tree2, (tree2_x, tree2_y))
        screen.blit(tree3, (tree3_x, tree3_y))
        screen.blit(tree4, (tree4_x, tree4_y))
        screen.blit(tree5, (tree5_x, tree5_y))
        
        # handling game over 
        if gameover:
            if playsound:     # condition for sounds
                sound=pygame.mixer.Sound('sounds/out.mp3')
                sound.play()
                playsound=False
            outro = pygame.image.load('sprites/outro.png').convert_alpha()
            screen.blit(outro, (210, 110))
            background_control = False
            tree_control = False
            jump = False
            walk_control = False
            dock_control = False
            jump_control = False
            screen.blit(bird[0], (bird1_x, bird1_y))
            screen.blit(bird[0], (bird2_x, bird2_y))
            screen.blit(dino4, (dino1_x, dino1_y))
            
            bird_move_control=False
            
            # handling keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()     # calling welcome function
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  
                        walk_control = False
                        dock_control = True
                    if event.key == pygame.K_c:   # Cheat Code [jump{up key} + C]
                        jump=False   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        walk_control = True
                        dock_control = False

        userinput = pygame.key.get_pressed()

        if jump_control == True:    # handling jump of player
            if jump is False and userinput[pygame.K_UP]:
                jump = True
                sound=pygame.mixer.Sound('sounds/jump.mp3')
                sound.play()
            if jump is True:
                dock_control = False
                walk_control = False
                dino1_y -= dino_y_vel*2    
                dino_y_vel -= 1
                if dino_y_vel < -10:  # restoring its original postition
                    jump = False
                    dino_y_vel = 10
                if jump == False:
                    walk_control = True

        # handling walk events
        if walk_control == True:
            screen.blit(walk[walkpoint], (dino1_x, dino1_y))
            walkpoint += 1
            if walkpoint > 5:
                walkpoint = 0

        elif dock_control == False and jump_control==True:
            screen.blit(dino1, (dino1_x, dino1_y))
        
        # handling dock events
        if dock_control == True:
            screen.blit(dock[dockpoint], (dock_x, dock_y))
            dockpoint += 1
            if dockpoint > 5:
                dockpoint = 0
        
        # handling bird events
        if bird_control == True and gameover== False:
            screen.blit(bird[birdpoint], (bird1_x, bird1_y))
            birdpoint += 1
            if birdpoint > 5:
                birdpoint = 0
        if bird2_control == True and gameover== False:
            screen.blit(bird[bird_2_point], (bird2_x, bird2_y))
            bird_2_point += 1
            if bird_2_point > 5:
                bird_2_point = 0

        if bird_move_control==True:    # moving birds horizontly
            bird1_x -= bird1_x_change
            bird2_x -= bird2_x_change
        if tree_control == True:    # moving trees horizontly
            tree1_x -= tree1_x_change
            tree2_x -= tree2_x_change
            tree3_x -= tree3_x_change
            tree4_x -= tree4_x_change
            tree5_x -= tree5_x_change
        
        # randomly blitting trees after collision using random module
        if tree1_x < -2900:
            tree1_x = random.randint(570, 580)
        if tree2_x < -2200:
            tree2_x = random.randint(1200, 1250)
        if tree3_x < -1700:
            tree3_x = random.randint(1700, 1760)
        if tree4_x < -1200:
            tree4_x = random.randint(2200, 2260)
        if tree5_x < -570:
            tree5_x = random.randint(2900, 2970)
        if bird1_x < -690:
            bird1_x = random.randint(3700, 3710)
        if bird2_x < -190:
            bird2_x = random.randint(6600, 6610)
        
        # condition for calling birds 
        if score>100:
            bird_control=True
        if score>320:
            bird2_control=True

        # handling collision events
        collision = iscollision(dino1_x, dino1_y, tree1_x, tree1_y)
        if collision:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, tree2_x, tree2_y)
        if collision:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, tree3_x, tree3_y)
        if collision:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, tree4_x, tree4_y)
        if collision:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, tree5_x, tree5_y)
        if collision:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, bird1_x, bird1_y)
        if collision and walk_control==True:
            gameover = True
        collision = iscollision(dock_x, dock_y, bird1_x, bird1_y)
        if collision and dock_control==True:
            gameover = True
        collision = iscollision(dino1_x, dino1_y, bird2_x, bird2_y)
        if collision:
            gameover = True
        
        # handling hiscore
        if gameover==False:
            text_screen("HI "+str(hiscore) + " " + str(score),(83,83,83),440,20)
        
        with open("hiscore.txt","w") as f:
            f.write(str(hiscore))      # storing hiscore on hiscore.txt file
        if gameover==True:
            if score>int(hiscore):
                hiscore=score
            text_screen("HI "+str(hiscore) + " " + str(score),(83,83,83),440,20)

        # increasing speed of sprites
        if score>i:
            tree1_x_change += 1
            tree2_x_change += 1
            tree3_x_change += 1
            tree4_x_change += 1
            tree5_x_change += 1
            bird1_x_change += 1
            bird2_x_change += 1
            background_change += 1
            i=i+100

        if score>int(hiscore):   # condition for handling score sound
            if playsound_1:
                sound=pygame.mixer.Sound('sounds/score.mp3')
                sound.play()
                playsound_1=False
        
        pygame.display.update()    # updating...
        clock.tick(fps)

welcome()   # calling welcome function
pygame.quit()    
quit()

# Thank You for using my code .
