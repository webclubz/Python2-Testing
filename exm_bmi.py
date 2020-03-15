# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:16:25 2020
@author: Economou Ath
Project Title: BMI
"""
name = "user"
height = 1.73
weight = 90

bmi = weight / (height **2)

if bmi < 25:
  print(name)
  print("KANONIKO BAROS")
else:
  print("BAROS PANO APO TO FYSIOLOGIKO")
  
  