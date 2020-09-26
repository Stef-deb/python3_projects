#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import socket
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import time, os, subprocess, threading

tcp = False
s = None
conn = None
ip = None
port = 8080
p = None
ip1 = None
port1 = None
path = None

class MainApp(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #toolbar

        self.tlbr = Button(background_down = "", background_normal = "", background_color = (0, 1, 0.6, 1), pos_hint={"center_x":0.5, "center_y":0.95}, size_hint= (1, 0.1))
        self.tlbr_txt = Label(text = "TCP File Sender/Receiver", font_size = 40, pos_hint={"center_x":0.5, "center_y":0.95}, outline_color = (0, 0, 0, 1), outline_width = 2)

        #home
        self.txt = TextInput(text= "Insert only the device's ip and the sender port\n ex:192.168.1.100:1234", size_hint = (0.5, 0.117), multiline=False, pos_hint= {"center_x":0.5, "center_y":0.585}, on_double_tap= self.on_tach)
        self.txt.bind(on_text_validate=self.on_enter)
        self.txt2 = TextInput(text= "Insert only the other device's ip and the sender receiver\n ex:192.168.1.100:1234", size_hint = (0.5, 0.117), multiline=False, pos_hint= {"center_x":0.5, "center_y":0.465}, on_double_tap= self.on_tach2)
        self.txt2.bind(on_text_validate=self.on_enter2)
        self.txt3 = TextInput(text= "Insert storage files path", size_hint = (0.5, 0.05), multiline=False, pos_hint= {"center_x":0.5, "center_y":0.05}, on_double_tap= self.on_tach3)
        self.txt3.bind(on_text_validate=self.on_enter3)
        self.backgr_home = Button(background_down = "", background_normal = "", background_color = (0.3, 0.7, 1, 1))
        self.filmn_bt = Button(text= "FileManager", font_size = 24, size_hint = (0.2, 0.1),pos_hint= {"center_x":0.5, "center_y":0.83} , on_release= self.FileManager_add_Layout)
        self.server_bt = Button(text= "Start/stop Tcp", font_size = 24, size_hint = (0.2, 0.1),pos_hint= {"center_x":0.5, "center_y":0.7} , on_press= self.start_server)
        self.add_widget(self.backgr_home)
        self.add_widget(self.filmn_bt)
        self.add_widget(self.server_bt)
        self.add_widget(self.txt)
        self.add_widget(self.txt2)
        self.add_widget(self.txt3)

        #msg_console

        self.layout = GridLayout(cols=1, spacing=-80, size_hint_y=None)
        self.root = ScrollView(size_hint=(0.5, 0.3), pos_hint = {"center_x":0.5, "center_y":0.25})
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.btn1 = Label(text="scroll down to see the new logs", size_hint_y=None)
        self.layout.add_widget(self.btn1)
        for i in range(5):
            self.layout.bind(minimum_height=self.layout.setter('height'))
            self.btn = Label(text="", size_hint_y=None)
            self.layout.add_widget(self.btn)
        self.root.add_widget(self.layout)

        self.console_bckg = Button(background_down = "", background_normal = "", background_color = (0, 0, 0, 1), size = (Window.size), size_hint=(0.5, 0.3), pos_hint = {"center_x":0.5, "center_y":0.25})
        self.add_widget(self.console_bckg)
        #FileManager_backround

        self.backr = Button(background_down = "", background_normal = "", background_color = (0.3, 0.7, 1, 1))

        #FileManager

        self.rltvl = RelativeLayout()
        self.tlbr1 = Button(background_down = "", background_normal = "", background_color = (0, 1, 0.6, 1), pos_hint={"center_x":0.5, "center_y":0.95}, size_hint= (1, 0.1))
        self.tlbr_txt1 = Label(text = "TCP File Sender/Receiver", font_size = 40, pos_hint={"center_x":0.5, "center_y":0.95}, outline_color = (0, 0, 0, 1), outline_width = 2 )
        self.nk = FileChooserIconView(pos_hint = {"center_x":0.5, "center_y":0.4})
        self.btn = Button(text= "Invia", size_hint = (0.1, 0.1),pos_hint= {"center_x":0.4, "center_y":0.08} , on_press= self.load_from_fileChooser)
        self.btn1 = Button(text= "Home", size_hint = (0.1, 0.1),pos_hint= {"center_x":0.6, "center_y":0.08} , on_press= self.FileManager_remove_Layout)
        self.rltvl.add_widget(self.backr)
        self.rltvl.add_widget(self.nk)
        self.rltvl.add_widget(self.btn)
        self.rltvl.add_widget(self.btn1)
        self.rltvl.add_widget(self.tlbr1)
        self.rltvl.add_widget(self.tlbr_txt1)

        self.add_widget(self.tlbr)
        self.add_widget(self.tlbr_txt)
        self.add_widget(self.root)


    def load_from_fileChooser(self, fileChooser):
        try:
            var = self.nk.selection
            selection = self.nk.selection
            print (selection)
            print(selection[0])
            file = open(selection[0], "rb")
            file1 = file.read()
            file.close()
            selection = str(selection[0])
            print(selection)
            selection = selection.split("/")
            selection = selection[-1]
            file1 += b"HanDsHak3St3ffoFil3"
            conn.sendall(selection.encode("utf-8") + b"HanDsHak3St3ffoSep" + file1)
            print (f"Inviato il file :")
            print(var)
            self.layout.add_widget(Label(text = f"Inviato il file :", size_hint_y= None))
            self.layout.add_widget(Label(text = str(var), size_hint_y= None))
        except Exception as e:
            print ("Unable to send the file:")
            print(var)
            print(e)
            self.layout.add_widget(Label(text = "Unable to send the file:", size_hint_y= None))
            self.layout.add_widget(Label(text = str(var), size_hint_y= None))
            self.layout.add_widget(Label(text = str(e), size_hint_y= None))

    def FileManager_add_Layout(self, *args):
        self.add_widget(self.rltvl)

    def FileManager_remove_Layout(self, *args):
        self.remove_widget(self.rltvl)

    def start_server(self, *args):
        global s, conn, address, tcp
        if tcp == False:
            try:
                s = socket.socket()
                s.bind((ip, port))
                s.listen()
                s.settimeout(5)
                print(f"Listening {ip , port}")
                self.layout.add_widget(Label(text = f"Listening {ip, port}", size_hint_y= None))
                self.start_receiver()
                conn, client_addr = s.accept()
                print(f"Connected to {client_addr}")
                self.layout.add_widget(Label(text = f"Connected to {client_addr}", size_hint_y= None))
                tcp = True
            except Exception as e:
                print(e)
                self.layout.add_widget(Label(text = str(e), size_hint_y= None))
        else:
            try:
                conn.sendall(b"HanDsHak3St3ffoKillScR1p7")
                vrx = conn.recv(8192)
                if vrx == b"HanDsHak3St3ffoKillScR1p7Re7":
                    time.sleep(0.1)
                    conn.close()
                    s.close()
                    tcp = False
                    print ("Server  off")
                    self.layout.add_widget(Label(text = "Server off", size_hint_y= None))
            except Exception as e:
                print(e)
                self.layout.add_widget(Label(text = str(e), size_hint_y= None))

    def on_enter(self, value):
        try:
            global ip, port
            var = self.txt.text.split(":")
            ip = var[0]
            port = int(var[-1])
            print("set address: " + ip + " " + str(port))
            self.layout.add_widget(Label(text =("set address: " + ip + " " + str(port)), size_hint_y= None))
        except Exception as e:
            print(e)
            self.layout.add_widget(Label(text = str(e), size_hint_y= None))

    def on_enter2(self, value):
        try:
            global ip1, port1
            var = self.txt2.text.split(":")
            ip1 = var[0]
            port1 = int(var[-1])
            print("set address (receiver): " + ip + " " + str(port))
            self.layout.add_widget(Label(text =("set address(receiver): " + ip + " " + str(port)), size_hint_y= None))
        except Exception as e:
            print(e)
            self.layout.add_widget(Label(text = str(e), size_hint_y= None))

    def on_enter3(self, value):
        try:
            global path
            path = self.txt3.text
            print (f"storage directory: {self.txt3.text}")
            self.layout.add_widget(Label(text = (f"storage directory: {self.txt3.text}"), size_hint_y= None))
        except Exception as e:
            print(e)
            self.layout.add_widget(Label(text = str(e), size_hint_y= None))

    def on_tach(self, *args):
        self.txt.text = ""

    def on_tach2(self, *args):
        self.txt2.text = ""

    def on_tach3(self, *args):
        self.txt3.text = ""

    def start_receiver(self):
        global p
        p = threading.Thread(target=self.recvr)
        p.start()

    def recvr(s):
        global ip1, por1, path
        #selecting path
        try:
            os.chdir(path)
        except Exception as e:
            print(e)
        #initializing receiver
        try:
            s1 = socket.socket()
            s1.connect((ip1, port1))
            print ("connected")
        except Exception as e:
            print(e)
            s1.close()
        while True:
            var = s1.recv(8192)
            if  var == b"HanDsHak3St3ffoKillScR1p7":
                s1.sendall(b"HanDsHak3St3ffoKillScR1p7Re7")
                s1.close()
                break
            if var.endswith(b"HanDsHak3St3ffoFil3"):
                var1 = var
                var1 = var1.split(b"HanDsHak3St3ffoSep")
                var1[-1].replace(b"HanDsHak3St3ffoFil3", "")
                file = open(var1[0], "wb")
                file.write(var1[-1])
                file.close()
            else:
                var1 = var
                while True:
                    var = s1.recv(8192)
                    if not var.endswith(b"HanDsHak3St3ffoFil3"):
                        var1 += var
                    else:
                        var1 = var1.split(b"HanDsHak3St3ffoSep")
                        var1[-1].replace(b"HanDsHak3St3ffoFil3", "")
                        file = open(var1[0], "wb")
                        file.write(var1[-1])
                        file.close()
                        break

class TCP_Send_Receive(App):
    def build(self):
        return MainApp()

if __name__ == "__main__":
    TCP_Send_Receive().run()
