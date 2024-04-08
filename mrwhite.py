import random
import pandas as pd
#players=["Mario", "Luigi", "Giovanni", "Maria"]

incognito=1

# Estrai il valore delle due celle della riga random
#df = pd.read_csv("nomi_comuni_di_cose.csv")
#riga_random = df.sample(n=1)
#parola1,  parola2 = riga_random['parola1'].values[0],  riga_random['parola2'].values[0]


def roles(players):
    posiz=random.sample(range( len(players)+1), 1+incognito)

    dizionario_giocatori = {}

    for i in range(len(players)):
        
        if i == posiz[0]:
            dizionario_giocatori[players[i]] = "White"
        elif i in posiz[1:] :
            dizionario_giocatori[players[i]] = "incognito" 
        else:
            dizionario_giocatori[players[i]] = "civile"

    return dizionario_giocatori




def wordle(players,parola1, parola2):  
    #scelgo le parole
    

    ruoli=roles(players)
    
    parole = {player: ""  for player in players} #inizializzo il dizionario con i nomi dei giocatori
    for player in players:                       #aggiorno il dizionario con le parole
        if ruoli[player] == "civile":
            parole[player] = parola1
        elif ruoli[player] == "incognito":
            parole[player] = parola2
    return parole

#parole_game=wordle()
#print   (wordle())


def vote(player,ruoli,parola1,parola2):
    #ruoli=roles(players)
    if ruoli[player] == "White":
        print ("Mister White è stato trovato\n prova a indovinare la parola")
        tentativo = input("Inserisci la parola: ")
        if tentativo == parola1:
            print ("Mr Whithe Hai vinto")
            return
        else:
            print ("Hai perso")
            return
    elif ruoli[player] == "incognito":
        print ("Complimenti hai trovato un incognito")
        ruoli.pop(player)

    else: 
        print ("Oh no, hai ucciso un civile")
        ruoli.pop(str(player))
    return ruoli


def ordine_giocatori(players):
    ruoli=roles(players)
    ordine = random.sample(players, len(players))
    while ruoli[ordine[0]] == "White":
        ordine = random.sample(players, len(players))
    return ordine
#print (ordine_giocatori())




    