#!/usr/bin/env python3
from kivymd.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from random import randint

lista = "numeri : "
somma = []
hai_selezionato = "hai selezionato: "

class MainApp(FloatLayout):

    def __init__(self,*args):
        super().__init__(*args)
        self.hint_label = Label(text="Tira i dadi!",font_size=24, pos= (0, 280))
        self.main_label = Label(text="",font_size=18, text_size=((self.width --600),(None)), pos= (-10, 100))
        self.second_label = Label(text= "" ,font_size=18, pos= (-300, 280))
        self.third_label = Label(text="",font_size=12,  text_size=((self.width --600),(None)), pos= (-10, -100))
        self.add_widget(self.hint_label)
        self.add_widget(self.main_label)
        self.add_widget(self.second_label)
        self.add_widget(self.third_label)
        self.add_widget(Button(text="D-4", pos= (30, 50), size_hint= (0.1, 0.1), on_press=self.D4))
        self.add_widget(Button(text="D-6", pos= (140, 50), size_hint= (0.1, 0.1), on_press=self.D6))
        self.add_widget(Button(text="D-8", pos= (250, 50), size_hint= (0.1, 0.1), on_press=self.D8))
        self.add_widget(Button(text="D-10", pos= (360, 50), size_hint= (0.1, 0.1), on_press=self.D10))
        self.add_widget(Button(text="D-12", pos= (470, 50), size_hint= (0.1, 0.1), on_press=self.D12))
        self.add_widget(Button(text="D-20", pos= (580, 50), size_hint= (0.1, 0.1), on_press=self.D20))
        self.add_widget(Button(text="D-100", pos= (690, 50), size_hint= (0.1, 0.1), on_press=self.D100))
        self.add_widget(Button(text="clear", pos= (700, 500), size_hint= (0.1, 0.1), on_press=self.clear ))


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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D4"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D6"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D8"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -10"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D12"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D20"
        self.third_label.text = hai_selezionato

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
        lista += self.ind + ", "
        self.main_label.text = lista
        somma1 = str(somma[0])
        self.second_label.text = "totale: " + somma1
        hai_selezionato += " -D100"
        self.third_label.text = hai_selezionato

    def clear(self,*args):
        global lista
        global somma
        global hai_selezionato
        lista = "numeri: "
        somma = []
        hai_selezionato = "hai selezionato: "
        self.main_label.text = lista
        self.second_label.text = ""
        self.third_label.text = ""



class Numeri(App):
    def build(self):
        return MainApp()

Numeri().run()
