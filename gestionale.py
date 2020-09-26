#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from datetime import datetime

# set config

from kivy.config import Config

Config.set('graphics', 'height', '720')
Config.set('graphics', 'width', '1280')

# vars
check1 = False
check = False
now = None

# outclass

vars_storage = JsonStore("vars_storage")

try:
    Num = vars_storage.get("Num")["n"]
except:
    vars_storage.put("Num", n = 1)
    Num = 1

data_storage = JsonStore("data_store")

# MainApp

class MainApp(FloatLayout):
    def __init__(self, **kwargs):
        global Num
        super().__init__(**kwargs)

        # background,toolbar
        self.title = Label(text = "Gestionale", font_size = 40, outline_color = (0,0,0,0), outline_width = 2, pos_hint = {"center_x":0.5, "center_y":0.966})
        self.background = Button(background_color = (1,1,1,1), background_normal = "", background_down = "")
        self.toolbar =  Button(background_color = (64/255, 121/255, 191/255, 1), background_normal = "", background_down = "", size_hint = (1, 0.07), pos_hint = {"center_x":0.5, "top":1})
        self.new_form = Button(text = "nuova scheda", pos_hint = {"center_x":0.93, "center_y":0.966}, size_hint = (0.1, 0.06), on_press = self.form_add)
        self.new_form.bind(size = self.resize)
        self.colors = Button(text = "colori", pos_hint = {"center_x":0.07, "center_y":0.966}, size_hint = (0.1, 0.06))
        self.add_widget(self.background)
        self.add_widget(self.toolbar)
        self.add_widget(self.title)
        self.add_widget(self.new_form)
        self.add_widget(self.colors)

        # form creator

        self.livello1 = RelativeLayout()
        self.title1 = Label(text = "Gestionale", font_size = 40, outline_color = (0,0,0,0), outline_width = 2, pos_hint = {"center_x":0.5, "center_y":0.966})
        self.toolbar1 =  Button(background_color = (191/255, 77/255, 64/255, 1), background_normal = "", background_down = "", size_hint = (1, 0.07), pos_hint = {"center_x":0.5, "top":1})
        self.background1 = Button(background_color = (1,1,1,1), background_normal = "", background_down = "")
        self.exit = Button(text = "Indietro", pos_hint = {"center_x":0.93, "center_y":0.966}, size_hint = (0.1, 0.06), on_press = self.form_add)
        self.label1 = Label(text = f"N : {Num} ", font_size = 20, pos_hint = {"center_x":0.04, "center_y":0.87}, outline_width = 2, outline_color = (0, 0, 0, 1))
        self.label2 = Label(text = "Data : ", font_size = 20, pos_hint = {"center_x":0.4, "center_y":0.87}, outline_width = 2, outline_color = (0, 0, 0, 1))
        self.label3 = Label(text = "Cliente : ", font_size = 20, pos_hint = {"center_x":0.7, "center_y":0.87}, outline_width = 2, outline_color = (0, 0, 0, 1))
        self.label4 = Label(text = "Commento: ", font_size = 20, pos_hint = {"center_x":0.5, "center_y":0.7}, outline_width = 2, outline_color = (0, 0, 0, 1))
        self.salva = Button(text = "salva", font_size = 20, pos_hint = {"center_x":0.5, "center_y":0.07}, size_hint = (0.1, 0.06), on_press = self.form_creator)
        self.textnpt1 = TextInput(pos_hint = {"center_x":0.86, "center_y":0.87}, size_hint = (0.2, 0.05), multiline = False)
        self.textnpt2 = TextInput(pos_hint = {"center_x":0.5, "center_y":0.4}, size_hint = (0.7, 0.5))
        self.livello1.add_widget(self.background1)
        self.livello1.add_widget(self.toolbar1)
        self.livello1.add_widget(self.title1)
        self.livello1.add_widget(self.exit)
        self.livello1.add_widget(self.label1)
        self.livello1.add_widget(self.label2)
        self.livello1.add_widget(self.label3)
        self.livello1.add_widget(self.textnpt1)
        self.livello1.add_widget(self.textnpt2)
        self.livello1.add_widget(self.label4)
        self.livello1.add_widget(self.salva)

        # alert

        self.alertliv = RelativeLayout()
        self.alertliv.add_widget(Button(background_color = (0,0,0,0.2), background_down = "", background_normal = ""))
        self.alertliv.add_widget(Button(background_color = (1,1,1,1), size_hint = (0.3, 0.3), background_down = "", background_normal = "", pos_hint = {"center_x":0.5, "center_y":0.5}))
        self.labello = Label(text = "       Ops!! non hai\n specificato il cliente!", outline_color = (0,0,0,1), outline_width = 2, font_size = 20, pos_hint = {"center_x":0.5, "center_y":0.58})
        self.ex = Button(text = "OK", pos_hint = {"center_x":0.5, "center_y":0.42}, font_size = 20, size_hint = (0.1, 0.1), on_press = self.alertus)
        self.alertliv.add_widget(self.labello)
        self.alertliv.add_widget(self.ex)

    # functions

    def resize(self, *args):
        if Window.size[0] < 955:
            self.new_form.text = "nuova\nscheda"
        else:
            self.new_form.text = "nuova scheda"

    def form_add(self, *args):
        global check, now
        if check == False:
            self.add_widget(self.livello1)
            now = datetime.now()
            now = now.strftime("%D - %H : %M : %S")
            self.label2.text = f"Data : {now}"
            check = True
        else:
            self.remove_widget(self.livello1)
            check = False

    def alertus(self, *args):
        global check1
        if check1 == False:
            self.add_widget(self.alertliv)
            check1 = True
        else:
            self.remove_widget(self.alertliv)
            check1 = False

    def form_creator(self, *args):
        global Num, now, check1

        if len(self.textnpt1.text) == 0:
            self.alertus()
        else:
            data_storage.put(str(Num), data = str(now), cliente = self.textnpt1.text, commento = self.textnpt2.text)
            Num = int(Num) + 1
            vars_storage.put("Num", n = Num)
            self.label1.text = str(Num)



class MyGest(App):
    def build(self):
        return MainApp()

MyGest().run()
