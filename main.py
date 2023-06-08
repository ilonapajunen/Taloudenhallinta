from datetime import datetime
import typing
from ui2_kayttoliittyma import Ui_Form as ui_form
from ui_lista import Ui_Form as lista_form
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets
import tietokanta


class Taloushallintasovellus(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui_form()
        self.ui.setupUi(self)
        self.lista = Talouslista()
        self.ui.button.clicked.connect(self.tallenna_tiedot)
        self.ui.naytaButton.clicked.connect(self.lista.show)

    def tallenna_tiedot(self):
        print("painettiin")
        self.nimi = self.ui.nimiKentta.text()
        self.summa = self.ui.summaKentta.text()
        try:
            self.summa = float(self.summa)
        except Exception:
            print("ei ole luku")
        self.paivamaara = datetime.now()
        tietokanta.tallenna_tiedot(self.nimi, self.summa, self.paivamaara)


class Talouslista(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = lista_form()
        self.ui.setupUi(self)
        self.nayta()

    def nayta(self):
        tiedot = tietokanta.nayta_tiedot()
        print(tiedot)
        for i in tiedot:
            self.ui.listWidget.addItem(i)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    talous_widget = Taloushallintasovellus()
    talous_widget.show() #jos ei laita showta, sitä ei näy käyttäjälle. löytyy myös hide()

    app.exec_() #ajaa sen 