
#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from random import randint
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel
from kivy.clock import Clock
from functools import partial
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.storage.jsonstore import JsonStore
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout


store = JsonStore('kivy_cache.json')
try:
    A = store.get("X")["C1"]
    B = store.get("X")["C2"]
    B1 = store.get("X")["B1"]
    B2 = store.get("X")["B2"]
    B3 = store.get("X")["B3"]
    B4 = store.get("X")["B4"]
    B5 = store.get("X")["B5"]
    B6 = store.get("X")["B6"]
except KeyError:
    store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (79/255, 231/255, 19/255, 1), B2 = (0, 217/255, 1, 1), B3 = (0, 217/255, 1, 1), B4 = (0, 217/255, 1, 1), B5 = (0, 217/255, 1, 1), B6 = (0, 217/255, 1, 1))
    A = store.get("X")["C1"]
    B = store.get("X")["C2"]
    B1 = store.get("X")["B1"]
    B2 = store.get("X")["B2"]
    B3 = store.get("X")["B3"]
    B4 = store.get("X")["B4"]
    B5 = store.get("X")["B5"]
    B6 = store.get("X")["B6"]

K = Window.size[1]*0.914
var = []
lista = "Numeri : "
somma = []
hai_selezionato = "Hai selezionato: "
larg = Window.size[0]
alt = Window.size[1]*0.9775
altrl = Window.size[1]
contr = False
contr1 = False
page = False

class MainApp(FloatLayout):
    def __init__(self,*args):
        super().__init__(*args)

#Tendina
        self.page_shadow = Button(background_color= (0,0,0,0.3),background_normal= "", background_down= "", pos = (0,0), size = (Window.size), on_press = self.Tend)
        self.page_shadow1 = Button(background_color= (0,0,0,0.3),background_normal= "", background_down= "", pos = (0,0), size = (Window.size), on_press = self.pagex)
        self.Tendina = RelativeLayout()
        self.alert = RelativeLayout()
        self.pagina1 = Button(background_color= (B),background_normal= "", background_down= "", pos = (0,0), pos_hint = {"center_x": 0.5, "center_y": 0.5} ,size_hint = (0.5,0.5) , on_press = self.pagex)
        self.temi = Label(text = "Temi",font_size=32, outline_color= (0,0,0,1), outline_width= 2, pos_hint ={"center_x": 0.66, "center_y": 0.75})
        self.lingua = Label(text = "Lingua", font_size=32, outline_color= (0,0,0,1), outline_width= 2, pos_hint ={"center_x": 0.66, "center_y": 0.55})
        self.sound = Label(text = "Suoni", font_size=32, outline_color= (0,0,0,1), outline_width= 2, pos_hint ={"center_x": 0.66, "center_y": 0.35})
        self.info = Label(text = "Info", font_size=32, outline_color= (0,0,0,1), outline_width= 2, pos_hint ={"center_x": 0.66, "center_y": 0.15})
        self.Title = Label(text="Menu",font_size=50,outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"center_x":0.6, "center_y":0.95})

#tend_buttons

        self.temi_bt = Button(size_hint= (0.055275, 0.035), background_color= (1,0,0,1),background_normal= "",background_down= "",pos_hint ={"center_x": 0.56, "center_y": 0.748}, on_press = self.pagex)
        self.lingua_bt = Button(size_hint= (0.055275, 0.035), background_color= (1,0,0,1),background_normal= "",background_down= "",pos_hint ={"center_x": 0.56, "center_y": 0.548})
        self.sound_bt = Button(size_hint= (0.055275, 0.035), background_color= (1,0,0,1),background_normal= "",background_down= "",pos_hint ={"center_x": 0.56, "center_y": 0.348})
        self.info_bt = Button(size_hint= (0.055275, 0.035), background_color= (1,0,0,1),background_normal= "",background_down= "",pos_hint ={"center_x": 0.56, "center_y": 0.148})
        self.ics = Button(text= "X", background_color= (1,0,0,1),background_normal= "",background_down= "",size_hint = (0.04145625, 0.02625), pos_hint = {"center_x": 0.975, "center_y": 0.9845}, on_press=self.Tend )
        self.toolbar_tend = Button(background_color= (A),background_normal= "",background_down= "", pos_hint = {"x":0, "y": 0.9})

#temi

        self.default_theme = Label(text = "tema chiaro", outline_color= (0,0,0,1), outline_width= 2, pos_hint = {"center_x": 0.5, "center_y": 0.75})
        self.night_theme = Label(text = "tema notturno", outline_color= (0,0,0,1), outline_width= 2, pos = (larg*0.5, alt*0.5), pos_hint = {"center_x": 0.5, "center_y": 0.65})
        self.dark_theme = Label(text = "tema scuro", outline_color= (0,0,0,1), outline_width= 2, pos = (larg*0.5, alt*0.5), pos_hint = {"center_x": 0.5, "center_y": 0.55})
        self.color_theme1 = Label(text = "tema colorato 1", outline_color= (0,0,0,1), outline_width= 2, pos = (larg*0.5, alt*0.5), pos_hint = {"center_x": 0.5, "center_y": 0.45})
        self.color_theme2 = Label(text = "tema colorato 2", outline_color= (0,0,0,1), outline_width= 2, pos = (larg*0.5, alt*0.5), pos_hint = {"center_x": 0.5, "center_y": 0.35})
        self.color_theme3 = Label(text = "tema colorato 3", outline_color= (0,0,0,1), outline_width= 2, pos = (larg*0.5, alt*0.5), pos_hint = {"center_x": 0.5, "center_y": 0.25})
        self.default_themebt = Button(background_color= B1,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.75}, on_press = self.default_themefn)
        self.night_themebt = Button(background_color= B2 ,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.65}, on_press = self.night_themefn)
        self.dark_themebt = Button(background_color= B3 ,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.55}, on_press = self.dark_themefn)
        self.color_theme1bt = Button(background_color= B4 ,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.45}, on_press = self.color_theme1fn)
        self.color_theme2bt = Button(background_color= B5 ,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.35}, on_press = self.color_theme2fn)
        self.color_theme3bt = Button(background_color= B6 ,background_normal= "",background_down= "",size_hint = (0.3, 0.05), pos_hint = {"center_x": 0.5, "center_y": 0.25}, on_press = self.color_theme3fn)
#sfondi coi buttons

        self.background = Button(background_color= (B),background_normal= "", background_down= "" )
        self.add_widget(self.background)
        self.toolbar = Button(background_color= (A),background_normal= "", background_down= "",pos_hint={"x":0, "y":0.9})
        self.add_widget(self.toolbar)
        self.tend_button = (Button(background_color= (B),background_normal= "", background_down= "", pos = (0,0)))
#testi
        self.Tendina = RelativeLayout(pos = (-larg,0))
        self.hint_label = Label(text="Tira i dadi!",font_size=50,outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":0.37})
        self.main_label = Label(text="",font_size=32, text_size=((self.width --580),(None)),outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":0.15})
        self.second_label = Label(text= "" ,font_size=32, pos= (-13,480),outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":0.31})
        self.third_label = Label(text="",font_size=32,  text_size=((self.width --580),(None)),outline_width= 2, outline_color= (0,0,0,1), pos_hint= {"x":0, "y":-0.2})
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
        self.toolbutton = (Button(background_down= "img/toolbutton_light.png",background_normal= "img/toolbutton.png",pos_hint= {"x":0.0333, "y":0.92222}, size_hint= (0.2, 0.07), on_press=self.Tend))
        self.add_widget(self.toolbutton)
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
        self.add_widget(self.d12t)
        self.add_widget(self.d20t)
        self.add_widget(self.d100t)
        self.add_widget(self.Tendina)

#Aggiunte dei Widgets al RelativeLayout

        self.Tendina.add_widget(self.tend_button)
        self.Tendina.add_widget(self.toolbar_tend)
        self.Tendina.add_widget(self.ics)
        self.Tendina.add_widget(self.Title)
        self.Tendina.add_widget(self.temi)
        self.Tendina.add_widget(self.lingua)
        self.Tendina.add_widget(self.sound)
        self.Tendina.add_widget(self.info)
        self.Tendina.add_widget(self.temi_bt)
        self.Tendina.add_widget(self.lingua_bt)
        self.Tendina.add_widget(self.sound_bt)
        self.Tendina.add_widget(self.info_bt)

#Aggiunte dei Widgets alla page button
        self.alert.add_widget(self.page_shadow1)
        self.alert.add_widget(self.pagina1)
        self.alert.add_widget(self.default_themebt)
        self.alert.add_widget(self.dark_themebt)
        self.alert.add_widget(self.night_themebt)
        self.alert.add_widget(self.color_theme1bt)
        self.alert.add_widget(self.color_theme2bt)
        self.alert.add_widget(self.color_theme3bt)
        self.alert.add_widget(self.default_theme)
        self.alert.add_widget(self.dark_theme)
        self.alert.add_widget(self.night_theme)
        self.alert.add_widget(self.color_theme1)
        self.alert.add_widget(self.color_theme2)
        self.alert.add_widget(self.color_theme3)

    def D4(self,*args):
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
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
        global lista, somma, hai_selezionato
        lista = "Numeri: "
        somma = []
        hai_selezionato = "Hai selezionato: "
        self.main_label.text = ""
        self.second_label.text = ""
        self.third_label.text = ""

    def Tend(self,*args):
        global contr, contr1
        if contr == False:
            self.d100t.add_widget(self.page_shadow)
            anim = Animation(x = larg*-0.5, y = 0, duration = 0.3)
            anim.start(self.Tendina)
            contr1 = True
            contr = True
        else:
            self.d100t.remove_widget(self.page_shadow)

            anim = Animation(x = larg*-1, y = 0, duration = 0.3)
            anim.start(self.Tendina)
            contr = False
            if contr1 == True:
                self.d100t.remove_widget(self.page_shadow1)
                contr1 = False

    def pagex(self,*args):
        global page, contr1
        if page == False:
            self.add_widget(self.alert)
            page = True
            if contr1 == True:
                self.d100t.remove_widget(self.page_shadow)
                contr1 = False
        else:
            self.remove_widget(self.alert)
            page = False
            if contr1 == False:
                self.d100t.add_widget(self.page_shadow)
                contr1 = True

    def default_themefn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (79/255, 231/255, 19/255, 1), B2 = (0, 217/255, 1, 1), B3 = (0, 217/255, 1, 1), B4 = (0, 217/255, 1, 1), B5 = (0, 217/255, 1, 1), B6 = (0, 217/255, 1, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.pagina1.background_color = B
        self.background.background_color = B
        self.tend_button.background_color = B
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

    def night_themefn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (13/255, 0, 133/255, 1), C2 = (0/255, 93/255, 168/255, 1), B1 = (13/255, 0, 133/255, 1), B2 = (79/255, 231/255, 19/255, 1), B3 = (13/255, 0, 133/255, 1), B4 = (13/255, 0, 133/255, 1), B5 = (13/255, 0, 133/255, 1), B6 = (13/255, 0, 133/255, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.pagina1.background_color = B
        self.background.background_color = B
        self.tend_button.background_color = B
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

    def dark_themefn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (0, 217/255, 1, 1), B2 = (0, 217/255, 1, 1), B3 = (79/255, 231/255, 19/255, 1), B4 = (0, 217/255, 1, 1), B5 = (0, 217/255, 1, 1), B6 = (0, 217/255, 1, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

    def color_theme1fn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (0, 217/255, 1, 1), B2 = (0, 217/255, 1, 1), B3 = (0, 217/255, 1, 1), B4 = (79/255, 231/255, 19/255, 1), B5 = (0, 217/255, 1, 1), B6 = (0, 217/255, 1, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

    def color_theme2fn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (0, 217/255, 1, 1), B2 = (0, 217/255, 1, 1), B3 = (0, 217/255, 1, 1), B4 = (0, 217/255, 1, 1), B5 = (79/255, 231/255, 19/255, 1), B6 = (0, 217/255, 1, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

    def color_theme3fn(self,*args):
        global A, B, C, store
        store.put("X", C1 = (0, 217/255, 1, 1), C2 = (208/255, 249/255, 251/255, 1), B1 = (0, 217/255, 1, 1), B2 = (0, 217/255, 1, 1), B3 = (0, 217/255, 1, 1), B4 = (0, 217/255, 1, 1), B5 = (0, 217/255, 1, 1), B6 = (79/255, 231/255, 19/255, 1))
        A = store.get("X")["C1"]
        B = store.get("X")["C2"]
        B1 = store.get("X")["B1"]
        B2 = store.get("X")["B2"]
        B3 = store.get("X")["B3"]
        B4 = store.get("X")["B4"]
        B5 = store.get("X")["B5"]
        B6 = store.get("X")["B6"]
        self.default_themebt.background_color = B1
        self.night_themebt.background_color = B2
        self.dark_themebt.background_color = B3
        self.color_theme1bt.background_color = B4
        self.color_theme2bt.background_color = B5
        self.color_theme3bt.background_color = B6
        self.toolbar_tend.background_color = A
        self.toolbar.background_color = A

class Numeri(App):
    def build(self):
        return MainApp()
if __name__ == "__main__":

	Numeri().run()
