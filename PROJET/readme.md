Ce projet est principalement divisé en 3 fichiers python : 
 - Analyse.py
 - Entrée.py
 - Sorties.py



## 1. Analyse.py
Il s'agit du document principal dans lequel sont appelées 
les différentes fonctions d'entrée et de sortie.



## 2. entrée.py
Une fois le document trame.txt ouvert, on enregistre dans une 
liste les différentes traces commençant à l'offset 0000 et séparées en 
lignes de 16 octets (dont le début est donné par l'offset, ex: 0000, 0001, etc).

Ensuite, on enleve les offset, les spaces, les sauts de ligne 
et on concatène les traces dans une autre liste définitif.



## 3. sorties.py
On reçoit la trace à traiter et on passe les différents 
protocoles en décomposant la trace en toutes les octets 
pour être traduit dans l'information requisé.

Les protocoles sont les suivantes:
  - Ethernet
  - IP
  - UDP
  - DNS ou DHCP

L'information de chaque protocol est écrit dans le document AnalyseurDeTrames.txt
comme sortie de l'information. 
