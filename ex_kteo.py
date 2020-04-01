# -*- coding: utf-8 -*-
"""
1.	Σε ένα κεντρικό ΚΤΕΟ προσέρχονται για τεχνικό έλεγχο τριών τύπων οχήματα: Φορτηγά, Επιβατικά και Μοτοσυκλέτες. Οι τακτικοί πελάτες μπορούν να γίνουν μέλη του ΚΤΕΟ και να έχουν έκπτωση στο κόστος ελέγχου. Το κόστος ελέγχου υπολογίζεται σύμφωνα με τον παρακάτω πίνακα:

Τύπος οχήματος	Μέλη ΚΤΕΟ	Μη Μέλη ΚΤΕΟ
Φορτηγά	70	80
Επιβατικά	40	50
Μοτοσυκλέτες	25	30

Να γράψετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο, για μία συγκεκριμένη ημέρα: 
α. Να διαβάζει τον τύπο του οχήματος για κάθε όχημα που προσέρχεται καθώς και αν ο πελάτης είναι μέλος του ΚΤΕΟ ή όχι. Η διαδικασία αυτή τερματίζεται όταν δοθεί ως τύπος οχήματος η λέξη «TELOS».
(Για Φορτηγό θα διαβάζει το «F», για Επιβατικό το «E» και για Μοτοσυκλέτα το «M». Δεν απαιτείται έλεγχος εγκυρότητας εισαγωγής των δεδομένων.) 

β. Να υπολογίζει το πλήθος και τις εισπράξεις του ΚΤΕΟ για κάθε τύπο οχήματος και να τα εμφανίζει μεκατάλληλα μηνύματα. Για παράδειγμα:
   Φορτηγά        10       750 ευρώ
   Επιβατικά      20        900 ευρώ
   Μοτοσυκλέτες   10     295 ευρώ
(Οι παραπάνω τιμές, όπως και ο τρόπος εμφάνισης-στοίχισης δίνονται ενδεικτικά.) 

γ. Να υπολογίζει και να εμφανίζει το πλήθος όλων των οχημάτων καθώς και το συνολικό ποσό είσπραξης του ΚΤΕΟ.

δ.Να υπολογίζει και να εμφανίζει με κατάλληλο μήνυμα τον αριθμό των μελών του ΚΤΕΟ και των μη μελών που προσήλθαν για τεχνικό έλεγχο την συγκεκριμένη ημέρα.
"""

exit = False
countCar = 0; countMembersCar = 0; countTruck = 0; countMembersTruck = 0; countMoto = 0; countMembersMoto = 0

print """
EKSODOS = exit
EPIVATIKA = e
FORTHGA = f
MOTO = m
"""

while not exit:
    vType = raw_input("TYPOS OXHMATOS: ")
    if vType == "exit":
        exit = True

    if vType == "e":
        isMember = raw_input("EINAI MELOS? Y: ")
        if isMember == "y":
            pmCar= 40
            print "EINAI MELOS \nTIMH :", pmCar
            countMembersCar += 1
            carMembers = countMembersCar * int(pmCar)
        else :
            pCar = 50
            print "DEN EINAI MELOS \nTIMH :", pCar
            countCar += 1
            cars = countCar * int(pCar)

    if vType == "f":
        isMember = raw_input("EINAI MELOS? Y: ")
        if isMember == "y":
            pmTruck= 70
            print "EINAI MELOS \nTIMH :", pmTruck
            countMembersTruck += 1
            truckMembers = countMembersTruck * pmTruck
        else :
            pTruck = 80
            print "DEN EINAI MELOS \nTIMH :", pTruck
            countTruck += 1
            trucks = countTruck * pTruck

    elif vType == "m":
        isMember = raw_input("EINAI MELOS? Y: ")
        if isMember == "y":
            pmMoto= 25
            print "EINAI MELOS \nTIMH :", pmMoto
            countMembersMoto += 1
            motoMembers = countMembersMoto * pmMoto
        else :
            pMoto = 30
            print "DEN EINAI MELOS \nTIMH :", pMoto
            countMoto += 1
            motos = countMoto * pMoto

print "SYNOLA"
print "---------------------------"
print "AYTOKINHTA  :", countCar, "| SYNOLO : ", cars
print "AYTOKINHTA MELH  :", countMembersCar, "| SYNOLO : ", carMembers
print "FORTIGA  :", countTruck, "| SYNOLO : ", trucks
print "FORTIGA MELH  :", countMembersTruck, "| SYNOLO : ", truckMembers
print "MOTO  :", countMoto, "| SYNOLO : ", motos
print "MOTO MEMBERS  :", countMembersMoto, "| SYNOLO : ", motoMembers
print "---------------------------"
print "SYNOLO OXHMATON : ", countMembersCar + countMembersTruck + countMembersMoto + countCar + countTruck + countMoto  
print "SYNOLO EISPRAKSEON : ", cars + carMembers + trucks + truckMembers + motos + motoMembers
print "---------------------------"
print "SYNOLO MELON : ", countMembersCar + countMembersTruck + countMembersMoto
print "SYNOLO MH MELON : ", countMembersCar + countMembersTruck + countMembersMoto
