import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)



#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.button import *
from kivy.uix.boxlayout import *
from kivy.uix.floatlayout import *


import random
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

def callback(instance):
    print('The button <%s> is being pressed' % instance.text)



class TestApp(App):

    def build(self):
        global TabellenBlatt
        
        Kletterer = []

        AllesDatensaetze = TabellenBlatt.get_all_records()
        AnzahlZeilen = len(AllesDatensaetze)
        
        for x in range (3,AnzahlZeilen+1):
            Name = TabellenBlatt.cell(x,1).value + " " + TabellenBlatt.cell(x,2).value
            Kletterer.append(Name)

        layout = BoxLayout(orientation='vertical')
        
        for i in Kletterer:
            btn = Button(text=str(i))
            btn.bind(on_press=callback)
            layout.add_widget(btn)

        btn = Button(text="Back")
        btn.bind(on_press=callback)
        layout.add_widget(btn)
        return layout


TabellenListe = ["FinaleMannlich9","FinaleWeiblich9"]
Tabellenname = random.choice(TabellenListe)
TabellenBlatt = client.open(TabellenName).sheet1
TestApp().run()
