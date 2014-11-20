#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Projet GSB : fichier principal """

from collections import OrderedDict
from tkinter import *
from tkinter.ttk import Combobox

class Application(Tk):
    """ Application et GUI. """
    def __init__(self):
        Tk.__init__(self)
        self.title('Gestion des rapports de Visite')
        self.fullscreen = False

        # CONFIG
        self.configure(width=600, height=400)

        # MENU
        self.menu_options = OrderedDict([
            ('Login'  , self.login),
            ('Quit'         , self.close)
            ])

        self.menuStrip = Menu(self)
        for (_label, action) in self.menu_options.items():
            self.menuStrip.add_command(label=_label, command=action)
        self.config(menu=self.menuStrip)

        # BINDINGS
        self.bindings = OrderedDict([
            ('<F11>'     , self.toggle_fullscreen)
            ])
        
        for (key, action) in self.bindings.items():
            self.bind(key, action)

    def toggle_fullscreen(self, event):
        """ Same func for turning it on and off. """
        if not self.fullscreen:
            self.sizeBuffer = (self.winfo_height(), self.winfo_width())
            self.geometry(
                "{0}x{1}+0+0".format(
                    self.winfo_screenwidth(),
                    self.winfo_screenheight()
                    )
                )
            self.overrideredirect(1)
            self.focus_set()
            self.fullscreen = True
        else:
            self.overrideredirect(0)
            self.geometry(
                "{0}x{1}+0+0".format(
                    *self.sizeBuffer
                    )
                )
            del self.sizeBuffer
            self.fullscreen = False

    def close(self):
        """ Close application (not just root window.) """
        self.destroy()
        print('Quitting...')
        exit(0)

    def login(self):
        """ Login popup """

        # Pop login window :
        loginScreen = Tk()
        
        # Textboxes
        lblHost = Label(loginScreen, text='Host : ')
        lblHost.grid(row=0, column=0, sticky=NW)
        tbHost = Entry(loginScreen)
        tbHost.grid(row=0, column=1, sticky=NW)

        lblDB = Label(loginScreen, text='Database : ')
        lblDB.grid(row=1, column=0, sticky=NW)
        tbDB = Entry(loginScreen)
        tbDB.grid(row=1, column=1, sticky=NW)

        # Login button
        bnLogin = Button(loginScreen,
                         text='Login',
                         command=lambda:print(tbHost.get()))
        bnLogin.grid(row=4, column=1, sticky=SE)
            
        self.loginInfo = {
            'host':tbHost.get()
            }

# Test:
if __name__ == '__main__':
    lApplication = Application()
    

