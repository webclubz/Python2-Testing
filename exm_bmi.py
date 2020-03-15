# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:16:25 2020
@author: Economou Ath
Project Title: BMI
"""
name = "user"
height = input("DOSE YPSOS: ")
weight = input("DOSE BAROS: ")

bmi = weight / (height **2)

if bmi < 25:
  print name
  print "KANONIKO BAROS"
else:
  print "TO BAROS SOU EINAI PANO APO TO FYSIOLOGIKO"
  
  