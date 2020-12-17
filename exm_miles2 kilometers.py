# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:13:03 2020
@author: Economou Ath
Project Title:
"""

def con(miles):
  km = 1.6 * miles
  return km

exit = False

while not exit:
  inpM = input("EISAGOGI SE MILIA: ") 
  if inpM == 0:
    print "BYE!!!"
    exit = True
  else :
    km = con(inpM)
    print inpM,"m -->", km,"km"
