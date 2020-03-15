# -*- coding: utf-8 -*-

def line():
    print "===================================="

'''
THERMOKRASIES EVDOMADOS ERGASTHRIOU
Python version 2.7.17
By Economou Athanasios
'''
minimum = 45
maximum = -10
sum = 0
i = 0

for thermokrasies in range(7):
    line()
    temp = input("DOSE THERMOKRASIA HMERAS: ")
    sum = sum + temp
    i += 1.0
    
    if temp > maximum:
        maximum = temp
    if temp < minimum:
        minimum = temp

mesos = sum / i
max = maximum
min  = minimum
line()
print "MESH THERMOKRASIA: ", mesos
print "MEGALYTERH: ", max
print "MIKROTERH: ", min


    