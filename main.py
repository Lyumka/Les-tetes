from chiffrement import chiffrement
from dechiffrement import dechiffrement

choix = input("Souhaitez vous de [c]hiffrer ou [d]echiffrer un message?")
if choix == "c":
    msg = input("Entrez le message a chiffrer (en lettre capitales, sans espace ni ponctuation : ")
    msg_chiffre = chiffrement(msg)
    print(f"Le message chiffré est {msg_chiffre}.")
    break
elif choix == "d":
    msg = input("Entrez le message a dechiffrer (en lettres capitales, sans espace ni ponctuation) :")
    msg_clair = dechiffrement(msg)
    print(f"Le message en clair est {msg_clair}.")