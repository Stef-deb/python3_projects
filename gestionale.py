#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from datetime import datetime
from kivy.uix.scrollview import ScrollView

# outclass

vars_storage = JsonStore("vars_storage")

try:
    Num = vars_storage.get("Num")["n"]
except:
    vars_storage.put("Num", n = 1)
    Num = 1

data_storage = JsonStore("data_store")

# vars

check2 = False
check1 = False
check = False
now = None
customer_name = None
customer_numberz = len(data_storage)

# MainApp

class MainApp(FloatLayout):
    def __init__(self, **kwargs):
        global Num
        super().__init__(**kwargs)

        # background,toolbar
        self.title = Label(text = "Gestionale", font_size = 40, outline_color = (0,0,0,0), outline_width = 2, pos_hint = {"center_x":0.5, "center_y":0.966})
        self.background = Button(background_color = (1,1,1,1), background_normal = "", background_down = "")
        self.toolbar =  Button(background_color = (64/255, 121/255, 191/255, 1), background_normal = "", background_down = "", size_hint = (1, 0.07), pos_hint = {"center_x":0.5, "top":1})
        self.new_customer = Button(text = "nuovo cliente", pos_hint = {"center_x":0.93, "center_y":0.966}, size_hint = (0.1, 0.06), on_press = self.alertus)
        self.new_customer.bind(size = self.resize)
        self.colors = Button(text = "opzioni", pos_hint = {"center_x":0.07, "center_y":0.966}, size_hint = (0.1, 0.06))
        self.customer_number = Label(text = f"Numero di clienti : {customer_numberz}", font_size = 20, outline_color = (0,0,0,0), outline_width = 2, pos_hint = {"center_x":0.5, "center_y":0.866})
        self.add_widget(self.background)
        self.add_widget(self.toolbar)
        self.add_widget(self.title)
        self.add_widget(self.new_customer)
        self.add_widget(self.colors)
        self.add_widget(self.customer_number)

        # customers navigation

        self.widgets()
        self.add_widget(self.root)

        # new customer

        self.alertliv = RelativeLayout()
        self.alertliv.add_widget(Button(background_color = (0,0,0,0.2), background_down = "", background_normal = "", on_press = self.alertus))
        self.alertliv.add_widget(Button(background_color = (1,1,1,1), size_hint = (0.3, 0.3), background_down = "", background_normal = "", pos_hint = {"center_x":0.5, "center_y":0.5}))
        self.labellotxt = Label(text = "   Digita il nome\ndel nuovo cliente", outline_color = (0,0,0,1), outline_width = 2, font_size = 20, pos_hint = {"center_x":0.5, "center_y":0.61})
        self.labello = TextInput(size_hint = (0.2, 0.05), pos_hint = {"center_x":0.5, "center_y":0.52}, multiline = False)
        self.labello.bind(on_text_validate = self.save)
        self.ex = Button(text = "Salva", pos_hint = {"center_x":0.5, "center_y":0.42}, font_size = 20, size_hint = (0.1, 0.1), on_press = self.save)
        self.alertliv.add_widget(self.labello)
        self.alertliv.add_widget(self.ex)
        self.alertliv.add_widget(self.labellotxt)

        # customer_view

        self.livello1 = RelativeLayout()
        self.title2 = Label(text = "Gestionale", font_size = 40, outline_color = (0,0,0,0), outline_width = 2, pos_hint = {"center_x":0.5, "center_y":0.966})
        self.background2 = Button(background_color = (1,1,1,1), background_normal = "", background_down = "")
        self.toolbar2 =  Button(background_color = (191/255, 83/255, 64/255, 1), background_normal = "", background_down = "", size_hint = (1, 0.07), pos_hint = {"center_x":0.5, "top":1})
        self.exit = Button(text = "Indietro", pos_hint = {"center_x":0.93, "center_y":0.966}, size_hint = (0.1, 0.06), on_press = self.add_customer_view)
        self.edit = Button(text = "Elimina cliente", pos_hint = {"center_x":0.07, "center_y":0.966}, size_hint = (0.1, 0.06), on_press = self.alert3)
        self.livello1.add_widget(self.background2)
        self.livello1.add_widget(self.toolbar2)
        self.livello1.add_widget(self.exit)
        self.livello1.add_widget(self.edit)
        self.livello1.add_widget(self.title2)


        #delete alert

        self.alertliv3 = RelativeLayout()
        self.alertliv3.add_widget(Button(background_color = (0,0,0,0.2), background_down = "", background_normal = ""))
        self.alertliv3.add_widget(Button(background_color = (1,1,1,1), size_hint = (0.3, 0.3), background_down = "", background_normal = "", pos_hint = {"center_x":0.5, "center_y":0.5}))
        self.labello3 = Label(text = "Vuoi davvero eliminare\n il cliente e i relativi dati?", outline_color = (0,0,0,1), outline_width = 2, font_size = 20, pos_hint = {"center_x":0.5, "center_y":0.58})
        self.ex3 = Button(text = "Si", pos_hint = {"center_x":0.43, "center_y":0.42}, font_size = 20, size_hint = (0.1, 0.1), on_press = self.deletez)
        self.ex3_1 = Button(text = "No", pos_hint = {"center_x":0.57, "center_y":0.42}, font_size = 20, size_hint = (0.1, 0.1), on_press = self.alert3)
        self.alertliv3.add_widget(self.labello3)
        self.alertliv3.add_widget(self.ex3)
        self.alertliv3.add_widget(self.ex3_1)


    # functions

    def resize(self, *args):
        if Window.size[0] < 955:
            self.new_customer.text = "nuovo\ncliente"
            self.edit.text = "Elimina\ncliente"                    # adapt button test in function of window size
        else:
            self.new_customer.text = "nuovo cliente"
            self.edit.text = "Elimina cliente"

    def alertus(self, *args):
        global check
        if check == False:
            self.add_widget(self.alertliv)
            check = True                                  # add or remove the layout with "new_customer"
        else:
            self.remove_widget(self.alertliv)
            check = False

    def refresh(self, *args):
        self.layout.clear_widgets()
        self.widgets()
        self.remove_widget(self.root)           # refresh scrollview (removes and adds it)
        self.add_widget(self.root)

    def save(self, *args):
        data_storage.put(self.labello.text)
        self.alertus()
        self.labello.text = ""                   # creates new customer and refreshes scrollview
        self.refresh()
        self.cus_num()

    def add_customer_view(self, *args):
        global check1
        if check1 == False:
            self.add_widget(self.livello1)
            check1 = True                                         # adds layout with customer datas and options
        else:
            self.remove_widget(self.livello1)
            check1 = False

    def widgets(self, *args):
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.root = ScrollView(size_hint=(0.77, 0.7), pos_hint = {"center_x":0.5, "center_y":0.42})
        self.layout.bind(minimum_height=self.layout.setter('height'))
        var =[]
        for i in data_storage:
            var.append(i)
        var = sorted(var)                                                                           # creates scrollview with customers
        for i in var:
            def press(self, *args):
                global customer_name
                customer_name = self.text
            self.layout.bind(minimum_height=self.layout.setter('height'))
            self.btn = Button(text= i, size_hint_y=None, height=30, on_press = press)
            self.layout.add_widget(self.btn)
            self.btn.bind(on_press = self.add_customer_view)
        self.root.add_widget(self.layout)

    def alert3(self, *args):
        global check2
        if check2 == False:
            self.add_widget(self.alertliv3)
            check2 = True                            # adds a layout with "do you want really delete this customer?"
        else:
            self.remove_widget(self.alertliv3)
            check2 = False

    def deletez(self, *args):
        global customer_name
        data_storage.delete(customer_name)
        self.refresh()                             # function that deletes customer
        self.alert3()
        self.add_customer_view()
        self.cus_num()

    def cus_num(self, *args):
        global customer_numberz
        customer_numberz = len(data_storage)
        self.customer_number.text = f"Numero di clienti : {customer_numberz}"

class MyGest(App):
    def build(self):
        return MainApp()

MyGest().run()
