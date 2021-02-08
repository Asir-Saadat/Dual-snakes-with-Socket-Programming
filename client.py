import pygame
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


def score(player1,player2):
    font = pygame.font.Font("ka1.ttf", 20)
    text1=font.render("PLAYER1: "+str(player1),True,(0,255,0))
    win.blit(text1,[15,0])
    text2 = font.render("PLAYER2: " + str(player2), True, (0,255,0))
    win.blit(text2, [15, 30])



class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])+ ","+str(tup[2])


def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())

    if(  startPos[0]==0):
        p = Player(startPos[0],startPos[1],100,100,(0,255,0))
        p2 = Player(0,0,100,100,(255,0,0))
        clock = pygame.time.Clock()
    else:
        p2 = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
        p = Player(0, 0, 100, 100, (255, 0, 0))
        clock = pygame.time.Clock()


    while run:
        clock.tick(60)

        if( startPos[0]==1):
            p2Pos = read_pos(n.send(make_pos((p.x, p.y, 1))))
            p2.x = p2Pos[0]
            p2.y = p2Pos[1]
            p2.update()
            p.move()
        else:
            p2Pos = read_pos(n.send(make_pos((p2.x, p2.y , 0))))
            p.x = p2Pos[0]
            p.y = p2Pos[1]
            p.update()
            p2.move()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        redrawWindow(win, p, p2)

main()