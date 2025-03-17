from fonctions import *
import string

filin = open("trace.txt", "r")
trame = filin.readlines()
#print(clear_trm(trame))
print(trace_to_list(file2list("trace.txt")))
