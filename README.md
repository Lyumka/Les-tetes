### Projet d'introduction à GitHub (chiffre de César)

### 1. Le chiffre de César
Le chiffre de César est une méthode de chiffrement très simple utilisée par Jule César dans ses correspondances secrètes.
Pour obtenir le texte chiffré, on remplace simplement chaque lettre du texte en clair par la lettre qui se trouve i places plus loin dans l'alphabet "modulo 26".
Ainsi, A est remplacé par D, B par E, W par Z, X par A etc. On utilise parfois un décalage autre que 3.

### 2. Implémentaton
Dans ce projet on écrira :
- une fonction ```chiffrement(message)``` qui permet de chiffrer une chaîne de caractères (écrits en capitales);
- une fonction ```dechifrement(message_chiffre)````qui permet de déchiffre un chaîne de caractères (écrits en capitales);
- une fonction principale qui demande à l'utilisateur de choisir entre chiffrement et déchiffrement, avant de lui demander le texte( à chiffrer ou déchiffrer).

### 3. Fichiers
Il faudra donc créer trois fichiers : un fichier ```chiffrement.py```, un fichier ```dechiffrement.py``` et un fichier ```main.py```