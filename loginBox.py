#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Projet GSB """

from tkinter import *
from tkinter.ttk import Combobox

class LoginBox(Tk):
    """ Formulaire d'authentification. """
    def __init__(self):
        Tk.__init__(self)
        self.title('Authentification')
        
        # Textboxes
        lblHost = Label(self, text='Host : ')
        lblHost.grid(row=0, column=0, sticky=NW)
        self.tbHost = Entry(self)
        self.tbHost.grid(row=0, column=1, sticky=NW)

        lblDB = Label(self, text='Database : ')
        lblDB.grid(row=2, column=0, sticky=NW)
        self.tbDB = Entry(self)
        self.tbDB.grid(row=2, column=1, sticky=NW)

        # Login button
        bnLogin = Button(self,
                         text='Login',
                         command=self.login)
        bnLogin.grid(row=4, column=1, sticky=SE)

    def login(self):
        loginInfo = {
            'host'      : self.tbHost.get().strip(),
            'database'  : self.tbDB.get().strip()
            }
        print('DEBUG :\n' + str(loginInfo))


# Test :
if __name__ == '__main__':
    l = LoginBox()
