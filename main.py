import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
Male9 = client.open("FinaleMannlich9").sheet1

from operator import *
from pprint import *

from tkinter import *
root = Tk()

liste = []
x = 1

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class Kletterer:
    def __init__(self, Vorname, Nachname, FinalPunktzahl, PlatzierungVorrunde):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.FinalPunktzahl = FinalPunktzahl
        self.PlatzierungVorrunde = PlatzierungVorrunde


def main():
    global x
    x = 1
    AllesDatensaetze = Male9.get_all_records()
    AnzahlZeilen = len(AllesDatensaetze)

    while x <= AnzahlZeilen:

        string = "global x; Nummer = 'nummer' + str(x)"
        exec(string)

        #print(x)
        x+=1
        
        Vorname = Male9.cell(x,2).value
        Nachname = Male9.cell(x,3).value
        FinalPunktzahl = Male9.cell(x,4).value
        PlatzierungVorrunde = Male9.cell(x,5).value

        Nummer = Kletterer(Vorname,Nachname,FinalPunktzahl,PlatzierungVorrunde)
        liste.append(Nummer)

        



    # pprint(liste)
    # print("")
    liste.sort(key=attrgetter("FinalPunktzahl"), reverse=False)

    #pprint(liste)

    while liste != []:
        Objekt = liste.pop()
        Vorname = Objekt.Vorname
        Nachname = Objekt.Nachname
        FinalPunktzahl = Objekt.FinalPunktzahl
        PlatzierungVorrunde = Objekt.PlatzierungVorrunde
        tabelle = "%-20s %-20s %-2s %-2s" % (Vorname, Nachname, FinalPunktzahl, PlatzierungVorrunde)
        print(tabelle)
        widget = Label(root, text="Platzhalter")
        widget.pack
    print("")

while True:
    main()

#GUI auf Kivy Basis, Kivy ist installiert