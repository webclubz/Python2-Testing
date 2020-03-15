# -*- coding: utf-8 -*-

import sys

def line():
    print "===================================="

'''
Python  INPUT TO LIST
version 2.7.17
By Economou Athanasios
'''

lst=[]
telos=False

while not telos:
    inp=input('DOSE ARITHMO :')
    if inp==0:
        telos=True
    else:
        lst=[inp] + lst # ΠΡΟΣΘΕΤΕΙ ΤΟ INP ΣΤΗΝ ΑΡΧΗ ΤΗΣ ΛΙΣΤΑΣ
        #lst.append(inp) #ΠΡΟΣΘΕΤΕΙ ΤΟ INP ΣΤΟ ΤΕΛΟΣ ΤΗΣ ΛΙΣΤΑΣ

line()
print lst
line()