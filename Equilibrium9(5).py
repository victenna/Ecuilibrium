import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

ox, oy = 600,420
px,py=[0,20,1150,1150,20],[0,400,400,440,440]
cx,cy=[0,150,300,450,600,750,900,1050,1200],[0,420,420,420,420,420,420,420,420]
speed=[0,-7,8,0,-4,-2,0,5,2,0]
image=[0]*10
for i in range (1,10):
    image[i]=pygame.image.load('imageE'+str(i)+'.png')
    if i==8:
        image[i]=pygame.image.load('image_E8.png')
custom_cursor=pygame.image.load('cursor.png')

angle0=0
qx,qy=[0]*5,[0]*5
zx,zy=[0]*8,[0]*9

X,Y=[0,125,1010,0,255,425,545,865,715,100],\
     [0,330,300,0,285,350,420,285,255,600]

q,n=1,-1
text = ''
BLACK = (0, 0, 0)
RED = (255, 0, 0)
A,answer=0,0
font0 = pygame.font.SysFont(None, 60)
title = font0.render('Правило рычага, Момент сил', True, 'blue')
font0_2 = pygame.font.SysFont(None, 30)
your_answer=font0_2.render('Ответ внесите в прямоугольное окно',\
                           True, 'blue')

font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ правильный', True, RED)
right_answer=font.render('Правильный ответ = 90 кГ', True, RED)

while True:
    screen.fill('gray') #цвет экрана
    screen.blit(title,(70,100))
    screen.blit(your_answer,(120,150))
    n=n+1
    n1=n%20
    if n1==10:
        q=q*-1
    angle0=angle0+q  
    angle=angle0*3.14159/180

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
                A=text
            if event.key == pygame.K_RETURN:
                answer=int(A)
                text=''
#------------------------------------------------------            
    if answer==90:
        angle0=0
        q=0
        X,Y=[0,125,1010,0,255,425,545,865,715,100],\
             [0,330,300,0,285,350,420,285,255,600]

        screen.blit(right,(800,150))
    if answer!=90 and answer!=0:
        screen.blit(wrong,(800,150))
        screen.blit(right_answer,(720,700))
#----------------------------------------------------
    for i in range (1,9):
        Y[i]=Y[i]+speed[i]*q
    for i in range (1,5):
        qx[i] = ox + math.cos(angle) * (px[i] - ox) - math.sin(angle) * (py[i] - oy)
        qy[i] = oy + math.sin(angle) * (px[i] - ox) + math.cos(angle) * (py[i] - oy)
   
    for i in range (1,8):
        zx[i] = ox + math.cos(angle) * (cx[i] - ox) - math.sin(angle) * (cy[i] - oy)
        zy[i] = oy + math.sin(angle) * (cx[i] - ox) + math.cos(angle) * (cy[i] - oy)
#-----------------------------------------------------------    
    txt_surface = font.render(text, True, 'red')
    screen.blit(txt_surface, (880,55))
    pygame.draw.rect(screen, 'black',[850,50,130,40],4)
    screen.blit(custom_cursor,(870,50))
#--------------------------------------------------------------------    
    pygame.draw.polygon(screen, 'red', ((qx[1],qy[1]), (qx[2],qy[2]), (qx[3],qy[3]),(qx[4],qy[4])))
    for i in range (1,8):
        pygame.draw.circle(screen, 'blue', (zx[i],zy[i]), 5)
       
    for i in range (1,10):
        if i!=3:
            screen.blit(image[i],(X[i],Y[i]))
    if q==0:
        image[8]=pygame.image.load('imageE8.png')
        screen.blit(image[8],(X[8],Y[8]))
    pygame.display.flip()
    clock.tick(10)