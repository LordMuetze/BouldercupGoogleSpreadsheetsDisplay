import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
Male9 = client.open("FinaleMannlich9").sheet1


x=1 
Alles = Male9.get_all_records()
Anzahl = len(Alles)
print(Anzahl)