from tkinter import *
from tkinter.ttk import Combobox


class FormNouvRapport(Frame):
    """ Frame contenant le formulaire de consultation des rapports.
    C'est un widget destiné à être empaqueté dans une fenêtre ou un
    autre formulaire.
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

        leftFrame = LabelFrame(text="Liste des rapports de visite")

        # NUMERO
        tbNum = Entry(leftFrame, width=24)
        tbNum.insert(0, '12')  # Hydrater avec les propriétés du rapport
        tbNum.config(state='readonly')
        
        Label(leftFrame,
              text='Numéro de rapport : ').grid(row=0, column=0, sticky=SE)
        tbNum.grid(row=0, column=1, sticky=SE, pady=5)

        # PRATICIEN
        cbbPraticien = Combobox(leftFrame,
                                width=22,
                                values=['Alice', 'Bob', 'Charlie', 'Donald'])
        cbbPraticien.set('Alice')  # Hydrater avec les propriétés du rapport
        cbbPraticien.config(state='disabled')
        
        Label(leftFrame, text='Praticien : ').grid(row=1, column=0, sticky=SE)
        cbbPraticien.grid(row=1, column=1, sticky=SE, pady=5)

        # DATE
        tbDate = Entry(leftFrame, width=24)
        tbDate.insert(0, '16/12/2014')  # Hydrater avec les propriétés du rapport
        tbDate.config(state='readonly')
        
        Label(leftFrame, text='Date : ').grid(row=2, column=0, sticky=SE)
        tbDate.grid(row=2, column=1, sticky=SE, pady=5)

        # MOTIF
        cbbMotif = Combobox(leftFrame, width=22, values=[
            'Visite régulière',
            'Demande',
            'Nouveau produit'])
        cbbMotif.set('Visite régulière')  # Hydrater avec les propriétés du rapport
        cbbMotif.config(state='disabled')
        
        Label(leftFrame, text='Combo : ').grid(row=3, column=0, sticky=SE)
        cbbMotif.grid(row=3, column=1, sticky=SE, pady=5)

        pane.add(leftFrame)

        # BILAN
        rightFrame = LabelFrame(text="Bilan : ")
        txtBilan = Text(rightFrame, height=6, width=64)
        txtBilan.insert(0, 'Bla blabla bla.')
        txtBilan.config(state='disabled')
        
        txtBilan.grid(row=4, column=1, pady=5)

        # ECHANTILLONS
        # TODO

        pane.add(rightFrame)

        pane.grid(row=0, column=0)

# Test
if __name__ == '__main__':
    s = FormNouvRapport(Tk())
    s.grid(row=0, column=0)
