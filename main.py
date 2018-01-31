import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
Male9 = client.open("FinaleMannlich9").sheet1

#----------------------------------------------------------------------------------------------------

from operator import *
from pprint import *
import time
from tkinter import *

#----------------------------------------------------------------------------------------------------

liste = []
x = 1
tabelle = "\n %-15s %-20s %-30s\n" % ("Platz", "Ergebnis", "Name")
ROOT = Tk()
Textsize = int(50*(ROOT.winfo_screenheight()/1080+ROOT.winfo_screenwidth()/1920)/2)
ROOT.overrideredirect(True)
ROOT.geometry("{0}x{1}+0+0".format(ROOT.winfo_screenwidth(), ROOT.winfo_screenheight()))
ROOT.focus_set()  # <-- move focus to this widget
ROOT.bind("<Escape>", lambda e: e.widget.quit())

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class Kletterer:
    def __init__(self, Vorname, Nachname, FinalPunktzahl, T, VT, B, VB):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Name = Vorname + " " + Nachname
        self.FinalPunktzahl = FinalPunktzahl
        self.Rohergebnis = str(T) + "T" + str(VT) + " " + str(B) + "B" + str(VB)

#----------------------------------------------------------------------------------------------------


def main():
    global x
    global tabelle
    global liste
    x = 1
    AllesDatensaetze = Male9.get_all_records()
    AnzahlZeilen = len(AllesDatensaetze)


    LABEL = Label(ROOT,text=tabelle,font="Times "+str(Textsize)+" bold",justify=LEFT)
    LABEL.pack()
    ROOT.update()

    zeit1 = time.time()

    print("while x <= AnzahlZeilen:")

    while x <= AnzahlZeilen:

        # string = "global x; Nummer = 'nummer' + str(x)"
        # exec(string)

        print(x)
        x+=1
        
        Vorname = Male9.cell(x,2).value
        Nachname = Male9.cell(x,3).value
        FinalPunktzahl = Male9.cell(x,4).value
        T = Male9.cell(x,5).value
        VT = Male9.cell(x,6).value
        B = Male9.cell(x,7).value
        VB = Male9.cell(x,8).value

        Nummer = Kletterer(Vorname, Nachname, FinalPunktzahl, T, VT, B, VB)
        liste.append(Nummer)
        

    # pprint(liste)
    # print("")
    liste.sort(key=attrgetter("FinalPunktzahl"), reverse=False)

    #pprint(liste)
    tabelle = "\n %-15s %-20s %-30s\n" % ("Platz", "Ergebnis", "Name")

    i = 0
    z = 1
    PunktzahlAlt = None

    while liste != []:
        Objekt = liste.pop()
        Name = Objekt.Name
        FinalPunktzahl = Objekt.FinalPunktzahl
        Rohergebnis = Objekt.Rohergebnis

        if PunktzahlAlt == FinalPunktzahl:
            i += 0
            z += 1
            #print("True, y:\t",y)
            print("True, z:\t",z)
        else:
            i += z
            z = 1
            #print("False, y:\t",y)
            print("False, z:\t",z)
                    
        print("i:\t",i)
        PunktzahlAlt = FinalPunktzahl

        tabelle = tabelle + "\n %-15s %-20s %-30s" % (str(i), Rohergebnis, Name)
            

        #tabelle = tabelle +"\n"+ Name +"\t"+ FinalPunktzahl +"\t"+ PlatzierungVorrunde

    LABEL.destroy()
    ROOT.update()


while True:
    main()

#GUI auf Kivy Basis, Kivy ist installiert