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
            ('Login'    , 'Pas encore implémenté'),
            ('Quit'     , self.close)
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
        print('Quitting...')
        self.destroy()
        exit(0)

# Test:
if __name__ == '__main__':
    lApplication = Application()
    

