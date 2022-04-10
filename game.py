from pygame import *
w = 500
h= 500
img_back = '34'
img_player = '23'
img_ball = '12'
life_1 = 3
life_2 = 3
tik_took_1 = 0
tik_took_2 = 0
display.set_caption('ping pong')
window = display.set_mode((w, h))
background = transform.scale(image.load(img_back), (w,h))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == Quit:
            run = False



if not finish:
    window.blit(background,(0,0))
    display.update