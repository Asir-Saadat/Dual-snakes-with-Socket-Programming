import pygame
import time
import random
import pygame.freetype
pygame.freetype.init()
from network import Network



pygame.init()

display_width=800
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Slither')
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
blue=(0,0,255)
light_blue=(0,191,255)
light_green=(102,255,102)
purple=(255,0,255)
deep_red=(204,0,0)
light_red=(255,51,51)
deep_orange=(255,128,0)
light_orange=(255,178,102)



block_size=10

clock= pygame.time.Clock()

def draw_snake1(block_size,snakelist1):
    for XnY in  snakelist1[:-1]:
        pygame.draw.rect(gameDisplay, light_green, [XnY[0], XnY[1], block_size, block_size])
    pygame.draw.rect(gameDisplay, green, [snakelist1[-1][0], snakelist1[-1][1], block_size, block_size])

def draw_snake2(block_size,snakelist2):
    for XnY in  snakelist2[:-1]:
        pygame.draw.rect(gameDisplay, light_blue, [XnY[0], XnY[1], block_size, block_size])
    pygame.draw.rect(gameDisplay, blue, [snakelist2[-1][0], snakelist2[-1][1], block_size, block_size])

def invulnerable(block_size,snakelist1):
    for XnY in  snakelist1[:-1]:
        pygame.draw.rect(gameDisplay, light_red, [XnY[0], XnY[1], block_size, block_size])
    pygame.draw.rect(gameDisplay, deep_red, [snakelist1[-1][0], snakelist1[-1][1], block_size, block_size])

def double(block_size,snakelist1):
    for XnY in  snakelist1[:-1]:
        pygame.draw.rect(gameDisplay, light_orange, [XnY[0], XnY[1], block_size, block_size])
    pygame.draw.rect(gameDisplay, deep_orange, [snakelist1[-1][0], snakelist1[-1][1], block_size, block_size])


def text_objects(msg,color,sizi):
    font = pygame.font.Font("ka1.ttf", sizi)
    textSurface= font.render(msg, True,color)
    return textSurface,textSurface.get_rect()



def message_to_screen(msg,color,y_displace=0,sizi=0):

    textSurf,textRect= text_objects(msg,color,sizi)
    textRect.center= (display_width/2,display_height/2  + y_displace)
    gameDisplay.blit(textSurf,textRect)

   # screen_text=font.render(msg, True,color)
   # gameDisplay.blit(screen_text,[display_width/2,display_height/2])

def game_menu():
    intro=True
    choice=1

    while(intro):

        gameDisplay.fill(black)
        message_to_screen("SNAKESSSSS", red, -140, 50)
        message_to_screen("PLAY", red, -10, 30)
        message_to_screen("INSTRUCTIONS",red,40,30)
        message_to_screen("QUIT",red,90,30)
        if(choice==1):
            pygame.draw.rect(gameDisplay, red, [display_width/2 -45, display_height/2 +10, 90, 5])
        elif(choice==2):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 140, display_height / 2 + 60, 280, 5])
        elif(choice==3):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + 110, 90, 5])



        pygame.display.update()
        for event in pygame.event.get():
           if(event.type==pygame.QUIT):
               pygame.quit()
               quit()
           if(event.type==pygame.KEYDOWN):
               if(event.key==pygame.K_DOWN):
                   if(choice==3):
                       choice=1
                   else:
                       choice+=1
           if (event.type == pygame.KEYDOWN):
               if(event.key==pygame.K_UP):
                   if (choice == 1):
                       choice =3
                   else:
                       choice -= 1
           if (event.type == pygame.KEYDOWN):
               if(event.key==pygame.K_SPACE):
                   if (choice == 1):
                       gameloop()
                   elif(choice==3):
                       pygame.quit()
                       quit()


def score(player1,player2):
    font = pygame.font.Font("ka1.ttf", 20)
    text1=font.render("PLAYER1: "+str(player1),True,red)
    gameDisplay.blit(text1,[15,0])
    text2 = font.render("PLAYER2: " + str(player2), True, red)
    gameDisplay.blit(text2, [15, 30])



def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])+ ","+str(tup[2])


def gameloop():
    gameexit = True
    gameover= False

    player_score_1=0
    player_score_2=0

    gamechange=1

    fruit_change=0
    fruit_present=0
    fruit_eaten=0
    fruit_eaten_change=0
    fruit_number=0
    apple_change=0


    snakelist1 = []
    snake_length1=7
    snakelist2 = []
    snake_length2 = 7
    Apple_thickness = 10

    rand_Apple_x=round(random.randrange(0+50,display_width-Apple_thickness-10)/10.0)*10.0
    rand_Apple_y=round(random.randrange(0+75,display_height-Apple_thickness-20)/10.0)*10.0

    rand_Fruit_x=round(random.randrange(0+50,display_width-Apple_thickness-10)/10.0)*10.0
    rand_Fruit_y=round(random.randrange(0+75,display_height-Apple_thickness-10)/10.0)*10.0

    #run = True
    n = Network()
    startPos = read_pos(n.getPos())

    if( startPos[2]==0 ):
        lead_x_1 = startPos[0]
        lead_y_1 = startPos[1]
        lead_x_change_1 = 0
        lead_y_change_1 = 0
        lead_x_2 = 200
        lead_y_2 = 200
        lead_x_change_2 = 0
        lead_y_change_2 = 0
    else:
        lead_x_1 = 200
        lead_y_1 = 200
        lead_x_change_1 = 0
        lead_y_change_1 = 0
        lead_x_2 = startPos[0]
        lead_y_2 = startPos[1]
        lead_x_change_2 = 0
        lead_y_change_2 = 0

    apple_change=0
    fruit_change=0




    while(gameexit):

        while(gameover==True):
            if(gamechange==1):
                gamechange+=1
                gameexit = True
                gameover = False

                snakelist1 = []
                snake_length1 = 7
                snakelist2 = []
                snake_length2 = 7
                Apple_thickness = 10

                rand_Apple_x = round(random.randrange(0+60, display_width -30 - Apple_thickness) / 10.0) * 10.0
                rand_Apple_y = round(random.randrange(0+60, display_height -30 - Apple_thickness) / 10.0) * 10.0


                lead_x_1 = 600
                lead_y_1 = 400
                lead_x_change_1 = 0
                lead_y_change_1 = 0
                lead_x_2 = 200
                lead_y_2 = 200
                lead_x_change_2 = 0
                lead_y_change_2 = 0

            else:
                gameDisplay.fill(black)
                if(player_score_1>player_score_2):
                    message_to_screen("PLAYER 1 WINS", red, -60, 40)
                if (player_score_1 < player_score_2):
                    message_to_screen("PLAYER 2 WINS", red, -60, 40)
                if (player_score_1 == player_score_2):
                    message_to_screen("DRAW", red, -60, 40)


                message_to_screen("GAMEOVER",red,-10,50)
                message_to_screen("Q to quit , R to restart",blue,30,10)
                pygame.display.update()

                for event in pygame.event.get():
                    if(event.type==pygame.KEYDOWN):
                        if(event.key==pygame.K_q):
                            gameover=False
                            gameexit=False
                        if(event.key==pygame.K_r):
                            gameloop()

        if (startPos[0] == 0):
            p2Pos = read_pos(n.send(make_pos((lead_x_1, lead_y_1, 1))))
            lead_x_2 = p2Pos[0]
            lead_y_2 = p2Pos[1]
            #p2.update()
            #p.move()
        else:
            p2Pos = read_pos(n.send(make_pos((lead_x_2, lead_y_2, 0))))
            lead_x_1 = p2Pos[0]
            lead_y_1 = p2Pos[1]
            #p.update()
            #p2.move()


        for event in pygame.event.get():
           if(event.type==pygame.QUIT):
               gameexit=True
               gameover=True

            #FIRST SNAKE MOVEMENT
           if(event.type==pygame.KEYDOWN):
               if(event.key==pygame.K_LEFT):
                   if(gamechange==1):
                       if(lead_x_change_1==block_size and lead_y_change_1==0):
                          continue
                       if(snake_length1>7):
                           if(snakelist1[-1][1] == snakelist1[-2][1]):
                               continue

                       lead_x_change_1=-block_size
                       lead_y_change_1=0
                   else:
                       if (lead_x_change_2 == block_size and lead_y_change_2 == 0):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][1] == snakelist1[-2][1]):
                               continue
                       lead_x_change_2 = -block_size
                       lead_y_change_2 = 0

               elif(event.key==pygame.K_RIGHT):
                   if(gamechange==1):
                       if (lead_x_change_1 == -block_size and lead_y_change_1 == 0):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][1] == snakelist1[-2][1]):
                               continue

                       lead_x_change_1=block_size
                       lead_y_change_1=0
                   else:
                       if (lead_x_change_2 == -block_size and lead_y_change_2 == 0):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][1] == snakelist2[-2][1]):
                               continue
                       lead_x_change_2 = block_size
                       lead_y_change_2 = 0

               elif (event.key == pygame.K_UP):
                   if(gamechange==1):
                       if (lead_x_change_1 == 0 and lead_y_change_1 == block_size):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][0] == snakelist1[-2][0]):
                               continue

                       lead_y_change_1=-block_size
                       lead_x_change_1=0
                   else:
                       if (lead_x_change_2 == 0 and lead_y_change_2 == block_size):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][0] == snakelist2[-2][0]):
                               continue
                       lead_y_change_2 = -block_size
                       lead_x_change_2 = 0

               elif (event.key == pygame.K_DOWN):
                   if(gamechange==1):
                       if (lead_x_change_1 == 0 and lead_y_change_1 == -block_size):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][0] == snakelist1[-2][0]):
                               continue

                       lead_y_change_1=block_size
                       lead_x_change_1=0
                   else:
                       if (lead_x_change_2 == 0 and lead_y_change_2 == -block_size):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][0] == snakelist2[-2][0]):
                               continue
                       lead_y_change_2 = block_size
                       lead_x_change_2 = 0

               elif (event.key == pygame.K_a):
                   if(gamechange==1):
                       if (lead_x_change_2 == block_size and lead_y_change_2 == 0):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][1] == snakelist2[-2][1]):
                               continue
                       lead_x_change_2 = -block_size
                       lead_y_change_2 = 0
                   else:
                       if (lead_x_change_1 == block_size and lead_y_change_1 == 0):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][1] == snakelist1[-2][1]):
                               continue
                       lead_x_change_1 = -block_size
                       lead_y_change_1 = 0

               elif (event.key == pygame.K_d):
                   if(gamechange==1):
                       if (lead_x_change_2 == -block_size and lead_y_change_2 == 0):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][1] == snakelist2[-2][1]):
                               continue
                       lead_x_change_2 = block_size
                       lead_y_change_2 = 0
                   else:
                       if (lead_x_change_1 == -block_size and lead_y_change_1 == 0):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][1] == snakelist1[-2][1]):
                               continue
                       lead_x_change_1=block_size
                       lead_y_change_1=0

               elif (event.key == pygame.K_w):
                   if(gamechange==1):
                       if (lead_x_change_2 == 0 and lead_y_change_2 == block_size):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][0] == snakelist2[-2][0]):
                               continue
                       lead_y_change_2 = -block_size
                       lead_x_change_2 = 0
                   else:
                       if (lead_x_change_1 == 0 and lead_y_change_1 == block_size):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][0] == snakelist1[-2][0]):
                               continue
                       lead_y_change_1=-block_size
                       lead_x_change_1=0

               elif (event.key == pygame.K_s):
                   if(gamechange==1):
                       if (lead_x_change_2 == 0 and lead_y_change_2 == -block_size):
                           continue
                       if (snake_length2 > 7):
                           if (snakelist2[-1][0] == snakelist2[-2][0]):
                               continue
                       lead_y_change_2 = block_size
                       lead_x_change_2 = 0
                   else:
                       if (lead_x_change_1 == 0 and lead_y_change_1 == -block_size):
                           continue
                       if (snake_length1 > 7):
                           if (snakelist1[-1][0] == snakelist1[-2][0]):
                               continue
                       lead_y_change_1=block_size
                       lead_x_change_1=0


        lead_x_1+=lead_x_change_1
        lead_y_1+=lead_y_change_1

        lead_x_2 += lead_x_change_2
        lead_y_2 += lead_y_change_2

        if(lead_x_1>display_width-20):
            lead_x_1=10
        if(lead_x_1<10):
            lead_x_1=display_width-20
        if(lead_y_1>display_height-10):
            lead_y_1=10
        if(lead_y_1<10):
            lead_y_1=display_height-10

        if (lead_x_2 > display_width-20):
             lead_x_2 = 10
        if (lead_x_2 < 10):
            lead_x_2 = display_width-20
        if (lead_y_2 > display_height-10):
            lead_y_2 = 10
        if (lead_y_2 < 10):
            lead_y_2 = display_height-10


        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay,red,[rand_Apple_x,rand_Apple_y,Apple_thickness,Apple_thickness])

        pygame.draw.rect(gameDisplay,red,[0,0,5,600])
        pygame.draw.rect(gameDisplay,red,[795,0,5,600])

        if(fruit_eaten==0):
            if(fruit_present==0):
                fruit_change+=1
                if(fruit_change==200):
                    fruit_present=1
                    fruit_change=0
            if (fruit_present == 1):
                fruit_change += 1
                if (fruit_change == 70):
                    fruit_present = 0
                    fruit_change=0
                    rand_Fruit_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
                    rand_Fruit_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 10) / 10.0) * 10.0



        if(fruit_present==1):
            pygame.draw.rect(gameDisplay, purple, [rand_Fruit_x, rand_Fruit_y, Apple_thickness, Apple_thickness])

        snakehead1=[]
        snakehead1.append(lead_x_1)
        snakehead1.append(lead_y_1)
        snakelist1.append(snakehead1)

        snakehead2 = []
        snakehead2.append(lead_x_2)
        snakehead2.append(lead_y_2)
        snakelist2.append(snakehead2)

        if( len(snakelist1)>snake_length1):
            del snakelist1[0]

        if (len(snakelist2) > snake_length2):
            del snakelist2[0]


        apple_change+=1

        if(apple_change==200):
            apple_change=0
            rand_Apple_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
            rand_Apple_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 20) / 10.0) * 10.0


        if(fruit_eaten==1):
            fruit_eaten_change+=1

        if(fruit_eaten_change==120):
            fruit_eaten=0
            fruit_eaten_change=0
            fruit_number=0


        if (fruit_present == 1):
            if (snakelist1[-1][0] == rand_Fruit_x and snakelist1[-1][1] == rand_Fruit_y):
                fruit_eaten = 1
                fruit_present=0
                fruit_change=0

                rand_Fruit_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
                rand_Fruit_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 10) / 10.0) * 10.0
                fruit_number=random.randrange(1,3)

            if (snakelist2[-1][0] == rand_Fruit_x and snakelist2[-1][1] == rand_Fruit_y):
                fruit_present=0
                fruit_change=0

                rand_Fruit_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
                rand_Fruit_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 10) / 10.0) * 10.0

        for each_segment in snakelist1[:-1]:
            if(each_segment==snakehead1 and len(snakelist1)>7):
                gameover = True

        for each_segment in snakelist2[:-1]:
            if(each_segment==snakehead2 and len(snakelist2)>7):
                if(gamechange==1):
                    player_score_2-=5
                else:
                    player_score_1-=5

        if(fruit_eaten==0 or fruit_number==2):
            for each_segment in snakelist2:
                for each_segment2 in snakelist1:
                    if(each_segment==each_segment2):
                        gameover=True


        if(fruit_eaten==1):
            if(fruit_number==1):
                invulnerable(block_size, snakelist1)
            else:
                double(block_size,snakelist1)
        else:
            draw_snake1(block_size,snakelist1)

        draw_snake2(block_size, snakelist2)

        if (lead_x_1== rand_Apple_x and lead_y_1== rand_Apple_y):
            rand_Apple_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
            rand_Apple_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 20) / 10.0) * 10.0
            snake_length1 += 1
            apple_change=0

            if(gamechange==1):
                if(fruit_number==2):
                    player_score_1+=20
                else:
                    player_score_1+=10
            else:
                if(fruit_number==2):
                    player_score_2+=20
                else:
                    player_score_2+=10

        if (lead_x_2== rand_Apple_x and lead_y_2== rand_Apple_y):
            rand_Apple_x = round(random.randrange(0 + 50, display_width - Apple_thickness - 10) / 10.0) * 10.0
            rand_Apple_y = round(random.randrange(0 + 75, display_height - Apple_thickness - 20) / 10.0) * 10.0
            snake_length2 += 1
            apple_change=0





        score(player_score_1,player_score_2)

        pygame.display.update()
        clock.tick(20)






game_menu()
#gameloop()