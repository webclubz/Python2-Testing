#!python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:39:51 2020
@author: Economou Ath
Project Title: check if raw_input is int() or str
"""
ex = False

while not ex:
  val = raw_input("> ")
  
  try: # IF IS INT
    value = int(val)
    print value
    print type(value)
  except: #IF IS STRING
      value = val
      if value == "exit":
        print type(value)
        print "BYE BYE!!!"
        ex = True
      else:
        print type(value)
        print "Try again"

  