# -*- coding: utf-8 -*-

import sys

def line():
    print "===================================="

'''
Python  REVERSED INPUT TO LIST
version 2.7.17
By Economou Athanasios
'''

lst=[]
lst2=[]
telos=False

while not telos:
    inp = input('DOSE ARITHMO :')
    # έξοδος με 0
    if inp == 0:
        telos=True
    else:
        lst=[inp] + lst # input στην αρχή 
        lst2.append(inp) # input στο τέλος

line()
print lst
print lst2
line()