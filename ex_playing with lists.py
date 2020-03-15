#!python
# -*- coding: utf-8 -*-
"""
Project Title: PLAYNG WITH LISTS
@author: Economou Ath
"""
msg = """
-------------------
PLAYING WITH LISTS
-------------------
Commands:
print = TYPONEI TIS THETIKES & ARNHTIKES LISTES
sump = PROSTHESH LISTAS THETIKON ARITHMON
sumn = PROSTHESH LISTAS ARNHTIKON ARITHMON
clear = ADEIAZEI TIS LISTES
help = EMFANIZEI TO PARON MHNYMA
exit = EKSODOS
"""

print msg

exit = False
pos = []
neg = []

while not exit:
  inp = raw_input("KATAXWRHSH ARITHMOU: ")

  try:
    value = int(inp)
    
    if value > 0:
      pos.append(value) 
    
    elif value < 0:
      neg.append(value)
  
  except:
    value = inp

    if value == "print":
      print pos
      print neg
    
    elif value == "sump":
      sump = 0
      for nums in pos:
        sump += nums
      print sump
    
    elif value == "sumn":
      sumn = 0
      for nums in neg:
        sumn += nums
      print sumn
    
    elif value == "clear":
      del pos[:]
      del neg[:]
    
    elif value == "help":
      print msg
    
    elif value == "exit":
      print "BYE BYE !!!"
      exit = True
    
    else: 
      print "LATHOS TIMI :("


