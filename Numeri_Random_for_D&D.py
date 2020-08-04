#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from random import randint
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel
from kivy.clock import Clock
from functools import partial
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.uix.relativelayout import RelativeLayout
import os, subprocess

a = 0
b = 0
B = 0
A = [1]
K = Window.size[1]*0.914
var = []
var2 = []
clock = [0,0]
clock2 = [0,0]
lista = "Numeri : "
somma = []
hai_selezionato = "Hai selezionato: "
posiz = Window.size[0]*-1
posiz1= int(Window.size[0]*0.6)
#controllo statico risoluzione

#var = Window.size[1]
#clock = [0,var*0.915]
#print(clock)

#var1 = Window.size[0]
#clockx = [var,0]
#print(clock)



class MainApp(FloatLayout):
    def __init__(self,*args):
        super().__init__(*args)
        self.add_widget(self.Background())
        self.add_widget(self.Toolbar())
        self.hint_label = Label(text="Tira i dadi!",font_size=50,outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":0.37})
        self.main_label = Label(text="",font_size=32, text_size=((self.width --580),(None)),outline_width= 2, outline_color= (0,0,0,1), pos= (-8, 140))
        self.second_label = Label(text= "" ,font_size=32, pos= (-13,480),outline_width= 2, outline_color= (0,0,0,1))
        self.third_label = Label(text="",font_size=32,  text_size=((self.width --580),(None)),outline_width= 2, outline_color= (0,0,0,1), pos= (-8, -260))
        self.add_widget(self.hint_label)
        self.add_widget(self.main_label)
        self.add_widget(self.second_label)
        self.add_widget(self.third_label)
        self.add_widget(Label(text="Dadi per D & D",font_size=58,outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":0.46222}))
#buttons

        self.add_widget(Button(background_down= "img/d4_light.png",background_normal= "img/d4.png", pos_hint= {"x":0.0325, "y":0.03267},size_hint= (0.1155, 0.07), on_press=self.D4))
        self.add_widget(Button(background_down= "img/d6_light.png",background_normal= "img/d6.png", pos_hint= {"x":0.169, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D6))
        self.add_widget(Button(background_down= "img/d8_light.png",background_normal= "img/d8.png", pos_hint= {"x":0.3055, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D8))
        self.add_widget(Button(background_down= "img/d10_light.png",background_normal= "img/d10.png",pos_hint= {"x":0.442, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D10))
        self.add_widget(Button(background_down= "img/d12_light.png",background_normal= "img/d12.png",pos_hint= {"x":0.5785, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D12))
        self.add_widget(Button(background_down= "img/d20_light.png",background_normal= "img/d20.png",pos_hint= {"x":0.715, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D20))
        self.add_widget(Button(background_down= "img/d100_light.png",background_normal= "img/d100.png",pos_hint= {"x":0.8515, "y":0.03267}, size_hint= (0.1155, 0.07), on_press=self.D100))
        self.add_widget(Button(background_color= (255/255,85/255,13/255,1), text="clear",font_size=32,pos_hint= {"x":0.8066,"y": 0.922}, size_hint= (0.1155, 0.07), on_press=self.clear ))
        self.add_widget(Button(background_down= "img/toolbutton_light.png",background_normal= "img/toolbutton.png",pos_hint= {"x":0.0333, "y":0.92222}, size_hint= (0.2, 0.07), on_press=self.Tend))

#testi dei buttons / buttons texts

        self.d4t = Label(text="D-4", font_size=32, outline_width= 2,pos_hint= {"x":-0.41111, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d6t = Label(text="D-6", font_size=32, outline_width= 2,pos_hint= {"x":-0.27461, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d8t = Label(text="D-8", font_size=32, outline_width= 2,pos_hint= {"x":-0.13811, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d10t = Label(text="D-10", font_size=32, outline_width= 2,pos_hint= {"x":-0.00161, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d12t = Label(text="D-12", font_size=32, outline_width= 2,pos_hint= {"x":0.13489, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d20t = Label(text="D-20", font_size=32, outline_width= 2,pos_hint= {"x":0.27139, "y":-0.43067}, outline_color= (0,0,0,1))
        self.d100t = Label(text="D-100", font_size=32, outline_width= 2,pos_hint= {"x":0.40989, "y":-0.43067}, outline_color= (0,0,0,1))
        self.add_widget(self.d4t)
        self.add_widget(self.d6t)
        self.add_widget(self.d8t)
        self.add_widget(self.d10t)
        self.add_widget(self.d12t)
        self.add_widget(self.d20t)
        self.add_widget(self.d100t)
        self.add_widget(var1)

#menu



    class Toolbar(Label):
        def __init__(self,*args):
            super().__init__(*args)
            with self.canvas.before:
                Color(255/255,85/255,13/255,1) #RGB 93, 220, 196
                self.rectangled= Rectangle(pos=clock,size=(Window.size))
            self.bind(pos=self.update_rect, size=self.update_rect)
        def update_rect(self,*args):
            global clock
            self.rectangled.pos= clock
            self.rectangled.size= Window.size

    class Background(Label):
        def __init__(self,*args):
            super().__init__(*args)
            with self.canvas.before:
                Color(102/255,255/255,133/255,1) #RGB 93, 220, 196
                self.rectangled1= Rectangle(size=(Window.size))
            self.bind( size=self.update_rect1)
        def update_rect1(self,*args):
            self.rectangled1.size= Window.size


#uscita menu

    pression_2 = ListProperty([0, 0])

    def Tend(self,*args):
        global A, var1, posiz1, lista, somma, hai_selezionato
        lista = "Numeri: "
        somma = []
        hai_selezionato = "Hai selezionato: "
        self.main_label.text = ""
        self.second_label.text = ""
        self.third_label.text = ""
        if var1.pos[0] == posiz1 -1 or var1.pos[0] == 0:
            self.pression_2 = A
            A += A
            return A
            return True
            return super(CustomBtn, self).on_touch_down(touch)

    def rip3(self,*args):
        global var1
        global a,b
        a += 1
        b += 1
        var1.pos = (a,0)
        #print(var1.pos[0])

    def rip4(self,*args):
        global var1
        global a,b
        a -= 1
        b -= 1
        var1.pos = (a,0)
        #print(var1.pos[0])


    def on_pression_2(self, instance ,pos):
        global posiz1
        if a == 0:
            for i in range (1,posiz1):
                Clock.schedule_once(partial(self.rip3),i*0.0005)
        else:
            for i in range (1,posiz1):
                Clock.schedule_once(partial(self.rip4),i*0.0005)


# roll dei dadi

    def D4(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,4))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D4"
        self.third_label.text = hai_selezionato
        if len(lista) >= 600:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D6(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,6))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D6"
        self.third_label.text = hai_selezionato
        if len(lista) >= 600:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D8(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,8))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D8"
        self.third_label.text = hai_selezionato
        if len(lista) >= 600:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D10(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,10))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -10"
        self.third_label.text = hai_selezionato
        if len(lista) >= 550:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D12(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,12))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D12"
        self.third_label.text = hai_selezionato
        if len(lista) >= 550:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D20(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.ind = str(randint(1,20))
        self.indn = int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D20"
        self.third_label.text = hai_selezionato
        if len(lista) >= 550:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def D100(self,*args):
        global lista
        global somma
        global hai_selezionato
        self.lista1= ["10","20","30","40","50","60","70","80","90","100"]
        self.indzzz = randint(0,9)
        self.ind = str(self.lista1[self.indzzz])
        self.indn= int(self.ind)
        if len(somma) == 0:
            somma.append(self.indn)
        else:
            var = somma[0] + self.indn
            somma = []
            somma.append(var)
        lista += self.ind + ", " + "   "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D100"
        self.third_label.text = hai_selezionato
        if len(lista) >= 550:
            lista = "numeri: "
            somma = []
            hai_selezionato = "hai selezionato: "
            self.main_label.text = ""
            self.second_label.text = ""
            self.third_label.text = ""

    def clear(self,*args):
        global lista
        global somma
        global hai_selezionato
        lista = "Numeri: "
        somma = []
        hai_selezionato = "Hai selezionato: "
        self.main_label.text = ""
        self.second_label.text = ""
        self.third_label.text = ""

    def contr(self):
        global var
        global clock
        var = Window.size[1]
        clock = [0,var*0.915]
        #print(clock)

    Clock.schedule_interval(partial(contr),0.001)




class Stiic(RelativeLayout):
    global A,B,K,posiz
    def __init__(self,*args):
        super().__init__(*args)

        self.add_widget(Label(text= ("Menu"), font_size=32 ,outline_color= (0,0,0,1),outline_width= 2,pos_hint ={"center_x": -0.5, "center_y": 0.9633}))
        self.add_widget(Label(text= ("Themes"), font_size=32 ,outline_color= (0,0,0,1),outline_width= 2,pos_hint ={"center_x": -0.36, "center_y": 0.75}))
        self.add_widget(Label(text= ("Sound"), font_size=32 ,outline_color= (0,0,0,1),outline_width= 2,pos_hint ={"center_x": -0.36, "center_y": 0.55}))
        self.add_widget(Label(text= ("Info"), font_size=32 ,outline_color= (0,0,0,1),outline_width= 2,pos_hint ={"center_x": -0.36, "center_y": 0.35}))
        self.add_widget(Label(text= ("Language"), font_size=32 ,outline_color= (0,0,0,1),outline_width= 2,pos_hint ={"center_x": -0.36, "center_y": 0.35}))

        self.add_widget(Button(size_hint= (0.05,0.03), text= ("X") ,pos_hint ={"center_x": -0.10, "center_y": 0.974}, on_press= self.Tend))
        self.add_widget(Button(size_hint= (0.05,0.03), pos_hint ={"center_x": -0.5, "center_y": 0.747}, on_press= self.dir))
        self.add_widget(Button(size_hint= (0.05,0.03), pos_hint ={"center_x": -0.5, "center_y": 0.547}))
        self.add_widget(Button(size_hint= (0.05,0.03), pos_hint ={"center_x": -0.5, "center_y": 0.347}))
        self.add_widget(Button(size_hint= (0.05,0.03), pos_hint ={"center_x": -0.5, "center_y": 0.147}))

        with self.canvas.before:
            Color(1,1,1,1) #RGB 93, 220, 196
            self.rectanglez = Rectangle(pos=(posiz,0),size=(Window.size))
        self.bind(size=self.update_rect)
    def update_rect(self,*args):
        self.rectanglez.size= Window.size
        with self.canvas.before:
            Color(1,1,0,1) #RGB 93, 220, 196
            self.rectanglez2 = Rectangle(pos=(posiz,K),size=(Window.size))

    pression_2 = ListProperty([0, 0])

    def Tend(self,*args):
        global A, var1, posiz1
        if var1.pos[0] == posiz1 -1 or var1.pos[0] == 0:
            self.pression_2 = A
            A += A
            return A
            return True
            return super(CustomBtn, self).on_touch_down(touch)

    def rip4(self,*args):
        global var1
        global a,b
        a -= 1
        b -= 1
        var1.pos = (a,0)
        #print(var1.pos[0])


    def on_pression_2(self, instance ,pos):
        global posiz1
        for i in range (1,posiz1):
            Clock.schedule_once(partial(self.rip4),i*0.0005)

    def dir(self,*args):
        file1 = open("Android/data/brtf.txt","a")
        file1.close
var1 = Stiic()



class Numeri(App):
    def build(self):
        return MainApp()
if __name__ == "__main__":

	Numeri().run()
