# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def line():
    print "===================================="

'''
Python 2 String Replace
version 2.7.17
By Economou Athanasios
'''
line()

c = "Ελληνικά Δρώμενα"
print c #Ελληνικά Δρώμενα

c = c.replace("Δρώμενα", "Στοιχεία")
print c #Ελληνικά Στοιχεία

c = "Ελληνικά Δρώμενα Δρώμενα Δρώμενα Δρώμενα"
c = c.replace("Δρώμενα", "Στοιχεία", 2)
print c #Ελληνικά Στοιχεία Στοιχεία Δρώμενα Δρώμενα

line()

c = "ΑΥΤΗ ΕΙΝΑΙ ΜΙΑ ΠΡΟΤΑΣΗ"

c = c.replace("ΠΡΟ", "!@#$%")

print(c) #ΑΥΤΗ ΕΙΝΑΙ ΜΙΑ !@#$%ΤΑΣΗ

line()
