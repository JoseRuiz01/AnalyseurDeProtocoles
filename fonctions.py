import string


import string

def len_line(tab):
    "lit les offset, les converti puis determine la longueur de chaque ligne"
    for t in range(1, len(tab)) :
        if(len(tab[t-1][0])>2 and is_hex(tab[t-1][0])):
            a = int (tab[t-1][0],16)
            b = int (tab[t][0],16)
            l = b-a
            tab[t-1]= tab[(t-1)][0:l+1]
            verif_ligne(tab[t-1],l, t-1)
    return tab

def concat_ligne(trame):
	cpt = []
	for s in trame :
		for l in s:
			cpt.append(l)

	return cpt

def remove_non_hexa(tab):
    ""
    for sl in tab:
        for octet_hex in sl:
            if(is_hex(octet_hex) == False or len(octet_hex)<2 ):
                sl.remove(octet_hex)
        if (sl==[]):
            tab.remove(sl)
    return tab

def verif_ligne(ligne, length,t): #le faire avec une exception 
    if(len(ligne)-1==length):
        return True
    print("ligne num :"+str(t)+" not OK")
    exit()

def remove_offset(tab):
    for i in range(0,len(tab)):
        tab[i].remove(tab[i][0])
    return tab

def clear_trm(trame):
    "cette fonction lis les offset et delimite les paquets"

    
    tab= []

    for l in trame:
        tab.append(l.split(' '))

    tab=remove_non_hexa(tab)
    tab=len_line(tab)
    tab=remove_offset(tab)
    return tab


#Retourne True si le caractère passé en paramètre est un nombre hexadécimal et False sinon.
def is_hex(n):
    
    if len(n) != 1:
		return False

	if not("a" <= n.lower() <= "f" or "0" <= n <= "9"):
		return False

	return True

#Retourne True si l octet passé en paramètre est valide et False sinon
def octet_valide(octet):
	if (len(octet)!=2):
		return False
	
	for c in octet : 
		if not(is_hex(octet)):
			return False
				
	
	return True


#retourne True si l offset est valide et False sinon
def OffsetValide(offset):
	if (len(offset) < 3):
		return False
	
	for c in offset :
		if (not(is_hex(int(c)))):
			return False
	
	return True

def file2list(File):
	filin = open(File, "r")
	lignes = filin.readlines()
	return lignes
	

#retourne une liste de liste, prend en paramètre une trace et met chacune dans une liste
def trace_to_list(trace):
	liste_trame = [[]] #la liste résultante
	trame_tmp = [] #la trame courante


	#on parcours toutes les lignes de la trace
	for ligne in range(len(trace)-1) : 
		#on prend l'offset de chaque ligne et on le convertit en hexa
		offset_char = trace[ligne][0]
		offset_int = int(offset_char, 16)
		#si l'offset n'est pas valide on affiche un message d'erreur et on ignore la ligne
		if (not (OffsetValide(offset_char))):
			print("Erreur : offset invalide, ligne ignorée: ", ligne)
		print("ace")
		#si l'offset est valide alors on continue le traitement
		#si l'offset vaut 0 alors on commence le traitement d'une nouvelle trame 
		if offset_int == 0 : 
			print("sabo")
			while int(trace[ligne][0])!=0:
				print("luffy")
				trame_tmp.append(trace[ligne][:])
				ligne +=ligne
			#on traîte la trame puis l'ajoute à la liste
			trame_tmp = clear_trm(trame_tmp)
			liste_trame.append(trame_tmp)

		#on réinitialise la trame courante pour la prochaine trame à lire
		trame_tmp = []
	


	return liste_trame

		






	
