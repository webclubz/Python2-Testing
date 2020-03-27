# -*- coding: utf-8 -*-

def line():
    print "===================================="

'''
BATHMOLOGIA MATHITI
Python version 2.7.17
By Economou Athanasios
'''
close = False
max = 0
min = 20
sum = 0
mathimata = 0

name = raw_input("DOSE ONOMA MATHiTI: ")

while not close:

    inp = input("DOSE BATHMOLOGIA: ")
    
    if inp == 1000:
        close = True
    else:
        if inp not in range(0, 21):
            print "LATHOS VATHMOS"
        else:
            sum  = sum + inp
            mathimata += 1.0
            if inp < min:
                min = inp
            if inp > max:
                max = inp
            

mesos  = sum /mathimata

line()
print "VATHMOLOGIA TOY MATHITI: ", name
print "EKSETAZOMENA MATIMATA: ", mathimata
print "MESOS OROS: ", mesos
print "MEGALYTEROS VATHMOS: ", max
print "MIKROTEROS VATHMOS: ", min
line()


    