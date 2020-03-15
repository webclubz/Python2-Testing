# -*- coding: utf-8 -*-

def line():
    print "===================================="

'''
Python  INPUT TO LIST
version 2.7.17
By Economou Athanasios
'''

lst=[]
nlst=[]
plst=[]
telos=False

while not telos:
    inp=input('DOSE ARITHMO :')
    if inp==0:
        telos=True
    else:
        #lst=[inp] + lst # ΠΡΟΣΘΕΤΕΙ ΤΟ INP ΣΤΗΝ ΑΡΧΗ ΤΗΣ ΛΙΣΤΑΣ
        lst.append(inp) #ΠΡΟΣΘΕΤΕΙ ΤΟ INP ΣΤΟ ΤΕΛΟΣ ΤΗΣ ΛΙΣΤΑΣ
    if inp > 0:
        plst.append(inp)
    elif inp < 0:
        nlst.append(inp)

line()
print "LISTA :", lst
line()
print "THETIKOI :", plst
line()
print "ARNHTIKOI", nlst
line()