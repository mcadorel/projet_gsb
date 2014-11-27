#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Projet GSB """

from tkinter import *
from tkinter.ttk import Combobox
from model import Model


class LoginBox(Tk):
    """ Formulaire d'authentification. """
    def __init__(self):
        Tk.__init__(self)
        self.title('Authentification')
        self.userName = ''

        # Textboxes
        lblUser = Label(self, text='Utilisateur : ')
        lblUser.grid(row=0, column=0, sticky=NW)
        self.tbUser = Entry(self)
        self.tbUser.grid(row=0, column=1, sticky=NW)

        lblPW = Label(self, text='Mot de passe : ')
        lblPW.grid(row=2, column=0, sticky=NW)
        self.tbPW = Entry(self)
        self.tbPW.grid(row=2, column=1, sticky=NW)

        # Login button
        bnLogin = Button(self,
                         text='Login',
                         command=self.login)
        bnLogin.grid(row=4, column=1, sticky=S)

        # Cancel button
        bnLogin = Button(self,
                         text='Annuler',
                         command=self.cancel)
        bnLogin.grid(row=4, column=1, sticky=SE)  # TODO : better snap to grid

    def login(self):
        """ Renvoie False en cas d'échec, ou le nom d'utilisateur sinon. """
        inputLoginInfo = {
            'user':     self.tbUser.get().strip(),
            'password': self.tbPW.get().strip()
            }

        with open('connexion_info.txt') as loginInfo:
            host = loginInfo.readline().split(':')[1].strip()
            database = loginInfo.readline().split(':')[1].strip()
            user = loginInfo.readline().split(':')[1].strip()
            password = loginInfo.readline().split(':')[1].strip()
            self.model = Model(host, database, user, password)

        if inputLoginInfo['password'] == self.model.query("""
            SELECT mdp
            FROM VISITEUR
            WHERE identifiant = '{}';
            """.format(inputLoginInfo['user']
                       ))[0][0].strip():  # TODO : Ewww, rewrite ASAP
            res = inputLoginInfo['user']
        else:
            res = False

        self.userName = res

    def cancel(self):
        exit(0)


# Test :
if __name__ == '__main__':
    l = LoginBox()
