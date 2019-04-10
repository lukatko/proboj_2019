from easygame import *
import time
import random

start = time.time()
def_start = time.time()
srd_start = time.time()
kov_start = time.time()

zombo = load_image("images/zombo.png")

zombobground = load_image("images/zombobground.jpg")
macka=load_image("images/mnau.png")
srdiecko=load_image("images/srdce.png")
kovadlina=load_image("images/kovadlina.png")
meme=load_image("images/sad.png")

#music=load_audio('2.wav')

open_window("ezpz", 1100, 600)

def nakresli_obdlznik(sirka, vyska, zaciatok, farba):
    draw_polygon((zaciatok, 0), (sirka+zaciatok, 0), (sirka+zaciatok, vyska), (zaciatok, vyska), color = (farba, farba, farba, farba))

class Gulicka:
    def __init__(self):
        self.y = 600
        self.x = random.randint(20, 1050)
        self.start = time.time()
        draw_image(position = (self.x, self.y),scale=0.75, image = zombo)
    def pohni_dole(self, k, score):
        if time.time() - self.start > 0.001 - 0.001 * k:
            self.start +=  0.001 - 0.001 * k
            self.y -= 3.5+score*0.025
        draw_image(position = (self.x, self.y), scale=0.75,image = zombo)
    def pohni_kovadlinu(self, k, score,rychlost):
        if time.time() - self.start > 0.001 - 0.001 * k:
            self.start +=  0.001 - 0.001 * k
            self.y -= 3.5+score*0.025+rychlost
        draw_image(position = (self.x, self.y), scale=0.1,image = kovadlina)
    def pohni_srdiecko(self, k, score,rychlost):
        if time.time() - self.start > 0.001 - 0.001 * k:
            self.start +=  0.001 - 0.001 * k
            self.y -= 3.5+score*0.025+rychlost
        draw_image(position = (self.x, self.y), scale=0.1,image = srdiecko)

x = 0
should_quit = False
lst = []
lst.append(Gulicka())
srd = []
kov = []
k = 0
score = 0
zivoty = 3
state = 0

while not should_quit:
    if state == 0:
        #play_audio(music,channel=0,loop=True,volume=1)
        for event in poll_events():
            if type(event) is CloseEvent:
                should_quit = True

            if (type(event) is MouseMoveEvent):
                x = event.x
        nakresli_obdlznik(200, 100, x-100, 1)
        draw_image(zombobground, position = (600, 300))
        if time.time() - srd_start > 15:
            srd.append(Gulicka())
            srd_start += 15
        if time.time() - kov_start > 10:
            kov.append(Gulicka())
            kov_start += 10
        if(time.time() - def_start) > 8 and k != 1.5:
            def_start += 8
            k += 0.5
        if time.time() - start > 2:
            lst.append(Gulicka())
            pridaj=score*0.015+0.6
            if(pridaj>1.725):
                pridaj=1.725
            start += 2 - pridaj
        for i in kov:
            i.pohni_kovadlinu(k, score,3)
            if (i.x <= x + 100 and i.x >= x - 100 and i.y <= 140):
                state = 1
                kov.pop(0)
                fill(255, 255, 255)
                zivoty=0
            if (i.y < 40):
                kov.pop(0)
        for i in srd:
            i.pohni_srdiecko(k, score,1.5)
            if (i.x <= x + 100 and i.x >= x - 100 and i.y <= 140):
                srd.pop(0)
                zivoty += 1
            if (i.y < 40):
                srd.pop(0)
        for i in lst:
            i.pohni_dole(k, score)
            if (i.x <= x + 100 and i.x >= x - 100 and i.y <= 160):
                score += 1
                lst.pop(0)
                
            if (i.y <= 60):
                zivoty -= 1
                lst.pop(0)
                if (zivoty == 0):
                    state = 1
                    fill(255, 255, 255)
                    #draw_text("Prehral si", size = 100, font = "Times New Roman", position = (300, 200))
        if not should_quit:
            print(lst)
            draw_text("Skore: " + str(score), size = 15, font = "Times New Roman", position = (880, 580), color = (1, 0, 0, 1))
            draw_text("Zivoty " + str(zivoty), size = 15, font = "Times New Roman", position = (880, 560), color = (1, 0, 0, 1))
            #nakresli_obdlznik(200, 100, x-100, 1)
            draw_image(macka,position=(x,50),scale=0.18)
            next_frame()
    if state == 1:
        fill(255, 255, 255)
        draw_image(meme,position=(550,250),scale=2)
        draw_text("Prehral si", size = 100, font = "Times New Roman", position = (300, 300),color=(1,0,0.5,1))
        draw_text("Stlac Q na ukoncenie",size =32,font="Times New Roman",position=(380,250),color=(1,0.25,0,1))
        draw_text("Tvoje vysledne skore je :" +str(score), size=32,font="Times New Roman",position=(350,200),color=(1,0.25,0,1))
        for event in poll_events():
            if type(event) is CloseEvent:
                should_quit = True
            if(type(event) is KeyDownEvent):
                if(event.key=='Q'):
                    should_quit=True
        next_frame()
