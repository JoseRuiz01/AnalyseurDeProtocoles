from clear_trame import *

trame=clear_trm("trame.txt","r")
totalLen=0
headerIP=0

def concat_ligne(trm):
    cpt=[]
    for sl in trm:
        for l in sl:
            cpt.append(l)
    
    #print(cpt)
    return cpt


#----------------------------------------------------------------------------------------------------------------------


def typeEthernet(s):
    print("\tChamp Ethernet Type :",end='')
    if (s=="0800"):
        print("\tDoD Internet\t(0x800)")
    if (s=="0805"):
        print("\tX.25 niveau3\t(0x805)")
    if (s=="0806"):
        print("\tARP\t(806)")
    if (s=="08098"):
        print("\tAppletalk\t(8098)")

def ethernet(trm):
    print("Champ Ethernet :\n")
    mac_dst=""
    mac_src=""
    mac_type=""
    idc=0

    #Adresse MAC dst
    for i in range(6):
        mac_dst+=trm[i]
        if(i!=5):
            mac_dst+=":"
        idc+=1
    print("\tAdresse MAC dst :\t"+mac_dst)

    #Adresse MAC src
    for i in range (idc,12):
        mac_src+=trm[i]
        if(i!=11):
            mac_src+=":"
        idc+=1
    print("\tAdresse MAC src :\t"+mac_src)

    #Champ Ethernet Type
    for i in range(idc,idc+2):
        mac_type+=trm[i]
    idc+=2
    typeEthernet(mac_type)
    
    print("\n\n")
    return idc 


#----------------------------------------------------------------------------------------------------------------------


def version(trm, idc):
    tmp=trm[idc]
    v = int(tmp[0])
    if (v==4):
        print("\tVersion :\t\t0x4 (IPV4)")
    else:
        print("\tVersion :\t\t"+hex(v))
    
    return v

def ihl(trm, idc):
    tmp=trm[idc]
    ihl = int(tmp[1])
    print("\tIHL : \t\t\t"+hex(ihl))
    return ihl

def headerLength(vrs,ihl):
    print("\tHeader length : \t",end=''),
    headerIP=ihl*vrs
    print(headerIP, "bytes")
    return headerIP


def tos(trm,idc):
    print("\tTOS :\t\t\t"+hex(int(trm[idc])))
    return idc+1

def totalLength(trm,idc):
    tmp=""
    tmp+=trm[idc]
    tmp+=trm[idc+1]                  
    print("\tTotal length :\t\t",end='')
    print(hex(int(tmp,16)), end='')
    print("  ",int(tmp,16),"bytes") 
    totalLen=int(tmp,16)
    trm=trm[:int(tmp,16)+14]
    return idc+2

def identification(trm,idc):
    tmp=""
    tmp+=trm[idc]
    tmp+=trm[idc+1]
    print("\tIdentification :\t",end='')
    print(hex(int(tmp,16)))
    return idc+2


def flags(trm, idc):
    tmp=""
    tmp=trm[idc]
    tmp=bin(int(tmp,16)).zfill(8)
    print("\tFlags :")
    print("\t\t\tDon't Fragment:", end='')
    print(" "+tmp[1])
    print("\t\t\tMore Fragment :",end='')
    print(" "+tmp[2])
    return idc
    
def fragOffset(trm,idc):
    tmp=''
    tmp=trm[idc]
    print("\tFragment Offset :")
    return idc+2

def ttl(trm, idc):             
    print("\tTTL :\t\t",end=''),
    print(hex(int(trm[idc])))
    return idc+1

def protocol(trm,idc):
    print("\tProtocol :")
    tmp=trm[idc]
    return idc+1

def headerChk(trm, idc):
    print("\tHeader Cheksum :")
    return idc+2

def adrsIP(trm,idc):
    tmp=''
    print("\tAdresses IP :")
    print("\t\t\tIP src :")
    dst=trm[idc:idc+4]
    for l in dst:
        tmp+=l
        tmp+=':'
    tmp=tmp[:len(tmp)-1]
    print ("\t\t\t\t"+tmp)
    
    idc+=4

    tmp=''
    print("\t\t\tIP dst :")
    src=trm[idc:idc+4]
    for l in src:
        tmp+=l
        tmp+=':'
    tmp=tmp[:len(tmp)-1]
    print("\t\t\t\t"+tmp)
    return idc+4

def IP(trm, idc):
    print("Champ Internet Protocole :\n")
    #Version
    v=version(trm,idc)

    #IHL
    IHL=ihl(trm,idc)

    #header length
    headerLength(v,IHL)
    
    idc+=1
    #TOS
    idc=tos(trm,idc)

    #Total length
    idc=totalLength(trm, idc)
    
    #Identification
    idc=identification(trm,idc)


    #Flags
    idc=flags(trm,idc)

    #Frgement offset
    idc=fragOffset(trm,idc)


    #TTL
    idc=ttl(trm,idc)

    #Protol
    idc=protocol(trm,idc)

    #Header Checksum
    idc=headerChk(trm,idc)

    #adressesIP
    idc=adrsIP(trm,idc)




trame = concat_ligne(trame)
idc = ethernet(trame)
IP(trame,idc)