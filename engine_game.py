# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:39:51 2020
@author: Economou Ath
Project Title: Engine Game
"""
print "USE COMMANDS: start, stop, exit"
escape = False
status = False
while not escape:
    car = raw_input("Tell me... What? ")
  
    if car == "start":
      if status:
        print "Engine already Started !!!"
      else:
        status = True
        print "Engine Started..."
      
    elif car == "stop":
        if not status:
          print "Engine already Stoped !!!"
        else:
          status = False
          print "Engine Stoped !!!"

    elif car == "exit":
        print "BYE"
        escape = True
    else:
      print "WTF! -> TRY: start, stop, exit"
  