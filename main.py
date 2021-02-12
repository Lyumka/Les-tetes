from chiffrement import *
from dechiffrement import*

while True :
    choix = input("Souhaitez-vous [c]hiffrer ou [d]échiffrer un message ?")
    if choix == "c":
        msg = input("Entrez le message à chiffrer (en lettre capitales, sans espace ni ponctuation) : ")
        msg_chiffre = chiffrement(msg)
        print(f"Le message chiffré est {msg_chiffre}.")
        break
    elif choix == "d":
        msg = input("Entrz le message à déchiffrer (en lettre capitales, sans espace ni ponctuation) : ")
        msg_clair = dechiffrement(msg)
        print(f"Le message en clair est {msg_clair}.")
        break
    else :
        print("Recommencez s'il vous plaît.")