# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def line():
    print "===================================="

'''
Python 2 Join
version 2.7.17
By Economou Athanasios
'''

line()

colors = ['',"Red","Blue","Yellow","brown"]
colorsAdd = ' | The color is:'.join(colors)
print(colorsAdd)

line()

firstname = "Athanasios"
lastname = "Economou"
                                                   
twoStrings = (firstname,lastname)
                                                   
name = " ".join(twoStrings)
print(name)

line()