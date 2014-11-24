from tkinter import *
from tkinter.ttk import Combobox

class FormNouvRapport(Frame):
    """ Frame contenant le formulaire d'ajout d'un nouveau rapport.
    C'est un widget destiné à être empaqueté dans une fenêtre ou un autrre formulaire.
    Structure :
    <Frame>
      <PanedWindow>
        <leftFrame>
          <!-- The actual form -->
        </leftFrame>
        <rightFrame>
          <!-- The actual form -->
        </rightFrame>
      </PanedWindow>
    </Frame>
    """
    def __init__(self, master):
        Frame.__init__(self, master)

        pane = PanedWindow(orient=HORIZONTAL)

        leftFrame = LabelFrame(text="Nouveau rapport de visite")

        # NUMERO
        tbNum = Entry(leftFrame, width=24)
        Label(leftFrame, text='Numéro de rapport : ').grid(row=0, column=0, sticky=SE)
        tbNum.grid(row=0, column=1, sticky=SE, pady=5)

        # PRATICIEN
        cbbPraticien = Combobox(leftFrame, width=22,values=['Alice', 'Bob', 'Charlie', 'Donald'])
        Label(leftFrame, text='Praticien : ').grid(row=1, column=0, sticky=SE)
        cbbPraticien.grid(row=1, column=1, sticky=SE, pady=5)

        # DATE
        tbDate = Entry(leftFrame, width=24)
        Label(leftFrame, text='Date : ').grid(row=2, column=0, sticky=SE)
        tbDate.grid(row=2, column=1, sticky=SE, pady=5)

        # MOTIF
        cbbMotif = Combobox(leftFrame, width=22, values=['Visite régulière', 'Demande', 'Nouveau produit'])
        Label(leftFrame, text='Combo : ').grid(row=3, column=0, sticky=SE)
        cbbMotif.grid(row=3, column=1, sticky=SE, pady=5)

        pane.add(leftFrame)

        # BILAN
        rightFrame = LabelFrame(text="Bilan : ")
        txtBilan = Text(rightFrame, height=6, width=64)
        txtBilan.grid(row=4, column=1, pady=5)

        # ECHANTILLONS
        # TODO
        
        pane.add(rightFrame)

        pane.grid(row=0, column=0)
        

s = FormNouvRapport(Tk())
s.grid(row=0, column=0)
