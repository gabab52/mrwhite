import random
import pandas as pd
from mrwhite import roles, wordle, ordine_giocatori,vote
players=["Mario", "Luigi", "Giovanni", "Maria","Sandro"]  # poi sostintuire con input
incognito=1

df = pd.read_csv("nomi_comuni_di_cose.csv")
riga_random = df.sample(n=1)
parola1,  parola2 = riga_random['parola1'].values[0],  riga_random['parola2'].values[0]

ruoli=roles(players)   #ottengo diz {nome:ruolo}
print ((ruoli))

parole_game=wordle(players,parola1,parola2)   #ottengo diz {nome:parola}
print(ordine_giocatori(players))  
while len(ruoli.keys())>3:
    
    ruoli=vote(input("Chi vuoi eliminare?"),ruoli,parola1,parola2) #vote restituisce i nuovi ruoli
    print (ruoli)


#lista bug
# a volte mr white non viene assegnato