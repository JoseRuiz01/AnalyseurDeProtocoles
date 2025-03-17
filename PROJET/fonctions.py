import string

def len_line(tab):
	final_tab = []
	for t in range(1, len(tab)):
		a = int(tab[t-1][0], 16)
		b = int(tab[t][0], 16)
		
		l = b-a
		if verif_ligne(tab[(t-1)][0:l+1], l, t-1):
			final_tab.append(tab[t-1]) 
	
	final_tab.append(tab[t-1]) 
	return final_tab

def concat_ligne(trame):
	cpt = []
	for s in trame :
		for l in s:
			cpt.append(l)

	return cpt

def remove_non_hexa(tab):
    final_tab = []
    for sl in tab:
        sl = list(filter(lambda octet_hex: is_hex(octet_hex) == True or len(octet_hex)>=2,  sl))
        if (sl==[]):
            tab.remove(sl)
        else:
            final_tab.append(sl)
            
    return  final_tab

def verif_ligne(ligne, length,t): #le faire avec une exception 
    if(len(ligne)-1==length):
        return True
    print("ligne num :"+str(t)+" not OK")
    return False

def remove_offset(tab):
    for i in range(0,len(tab)):
        tab[i].remove(tab[i][0])
    return tab

def clear_trm(trame):
    #cette fonction lis les offset et delimite les paquets
    tab= []

    for l in trame:
        tab.append(l.split(' '))

    tab=remove_non_hexa(tab)
    tab=len_line(tab)
    tab=remove_offset(tab)
    return tab


#Retourne True si le caractère passé en paramètre est un nombre hexadécimal et False sinon.
def is_hex(n):

	if (len(n) != 1):
		return False

	if not("a" <= n.lower() <= "f" or 0 <= int(n) <= 9):
		return False

	return True

#Retourne True si l octet passé en paramètre est valide et False sinon
def octet_valide(octet):

	if (len(octet)!=2):
		return False
	
	for c in octet : 
		if not(is_hex(c)):
			return False
				
	
	return True


#retourne True si l offset est valide et False sinon
def OffsetValide(offset):
	if (len(offset) < 3):
		return False
	
	for c in offset :
		if (not(is_hex(str(c)))):
			return False
	
	return True



def file2list(File):
	#ouvre le fichier Trace.txt
	filin = open(File, "r")
	#enregistre chaque ligne du fichier dans une liste.
	lignes = filin.readlines()
	
	#retourne une liste avec les differentes lignes
	return lignes
	



#retourne une liste de liste, prend en paramètre une trace et met chacune dans une liste
def trace_to_list(trace):
	liste_trame = [] #la liste résultante
	trame_tmp = [] #la trame courante
	ligne = 0

	#on parcours toutes les lignes de la trace
	while ligne < (len(trace)): 

		offset_char = trace[ligne][0:4]
		offset_int = int(offset_char, 16)

		if (offset_int == 0):
			trame_tmp.append(trace[ligne][:])
			ligne += 1


		else:	
			#loop jusqu'à ce qu'on trouve un autre offset 0
			while offset_int != 0 and ligne < (len(trace)):
				#si ce n'est pas un offset valide, on montre le message d'erreur
				if (not (OffsetValide(offset_char))):
					print("Erreur : offset invalide, ligne ignorée: ", ligne)

				else:
					#sinon on ajoute cette ligne 
					trame_tmp.append(trace[ligne][:])

				#continue avec la ligne suivante
				ligne +=1

				if(ligne < len(trace)):
					#on prend l'offset de chaque ligne
					offset_char = trace[ligne][0:4]
					offset_int = int(offset_char, 16)
				
				
			trame_tmp = clear_trm(trame_tmp)
			#on sauvegarde le trame finale
			liste_trame.append(trame_tmp)
			#on réinitialise la trame courante pour la prochaine trame à lire
			trame_tmp = []


	return liste_trame
