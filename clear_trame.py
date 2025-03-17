import string

def len_line(tab):
    "lit les offset, les converti puis determine la longueur de chaque ligne"
    for t in range(1, len(tab)) :
        if(len(tab[t-1][0])>2 and is_hexa(tab[t-1][0])):
            a = int (tab[t-1][0],16)
            b = int (tab[t][0],16)
            l = b-a
            tab[t-1]= tab[(t-1)][0:l+1]
            verif_ligne(tab[t-1],l, t-1)
    return tab

def is_hexa(s):
    
    try:
        int(s,16)
        return True

    except ValueError:
        return False

def remove_non_hexa(tab):
    ""
    for sl in tab:
        for octet_hex in sl:
            if(is_hexa(octet_hex) == False or len(octet_hex)<2 ):
                sl.remove(octet_hex)
        if (sl==[]):
            tab.remove(sl)
    return tab

def verif_ligne(ligne, length,t): #le faire avec une exception 
    if(len(ligne)-1==length):
        return True
    print("ligne num :"+str(t)+" non OK")
    exit()

def remove_offset(tab):
    for i in range(0,len(tab)):
        tab[i].remove(tab[i][0])
    return tab

def clear_trm(file, r):
    "cette fonction lis les offset et delimite les paquets"

    filin = open(file,r)
    lignes = filin.readlines()
    tab= []

    for l in lignes:
        tab.append(l.split(' '))

    tab=remove_non_hexa(tab)
    tab=len_line(tab)
    tab=remove_offset(tab)
    return tab