import numpy
from random import shuffle
import pygame
def display(img,x,y):
    screen.blit(img,(x,y))
    pygame.display.update()
image={}
l=list(map(str,range(1,16)))
Check=l.copy()
shuffle(l)
l=l+['0',]
k=numpy.array(l).reshape((4,4))
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("OrderIt")
#icon=pygame.image.load('brain.png')
#pygame.display.set_icon(icon)
screen.fill((255,255, 255))
for i in range(1,16):
    image[str(i)]=pygame.image.load('Numbers\\'+str(i)+'.png')
for i in range(0,4):
    for j in range(0,4):
        if k[i,j] in image:
            display(image[k[i,j]],i*100,j*100)
running=True
print(k)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            x,y=x//100,y//100
            if x>0 and k[x-1,y]=='0': #left
                k[x,y],k[x-1,y]=k[x-1,y],k[x,y]
                for i in range(1,101):
                    display(image[k[x-1,y]],x*100-i,y*100)
            elif x<3 and k[x+1,y]=='0': # right
                k[x, y], k[x + 1, y] = k[x + 1, y], k[x, y]
                for i in range(1,101):
                    display(image[k[x+1,y]],x*100+i,y*100)
            elif y>0 and k[x,y-1]=='0': #up
                k[x, y], k[x, y-1] = k[x, y-1], k[x, y]
                for i in range(1,101):
                    display(image[k[x,y-1]],x*100,y*100-i)
            elif y<3 and k[x,y+1]=='0':#down
                k[x, y], k[x, y + 1] = k[x, y + 1], k[x, y]
                for i in range(1,101):
                    display(image[k[x,y+1]],x*100,y*100+i)
            if x==3 and y==3:
                S=list(k.T.reshape((1,16))[0])[:-1]
                if S==list(map(str,range(1,15))):
                    #win=pygame.image.load('win.png')
                    if event.type!=pygame.QUIT:
                        #pygame.display.update(win,0,0)
                        print("Game over")



