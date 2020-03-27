# -*- coding: utf-8 -*-
"""
sum = (vathPro*0.3) + (vathGra*0.7)
Β2. Για κάθε μαθητή δίνονται τα στοιχεία: ονοματεπώνυμο, προφορικός και γραπτός βαθμός ενός μαθήματος. Να γραφτεί πρόγραμμα σε Python που να εκτελεί τις παρακάτω λειτουργίες:
Β2.1. Να διαβάζει τα στοιχεία πολλών μαθητών και σταματά, όταν δοθεί ως ονοματεπώνυμο το κενό. Β2.2. Να ελέγχει αν ο προφορικός και ο γραπτός βαθμός είναι από 0 μέχρι 20. Στην περίπτωση που δεν είναι ο βαθμός στα επιτρεπτά όρια, να ξαναδιαβάζεται ο βαθμός μέχρι να δώσουμε τον σωστό βαθμό.
Β2.3. Να υπολογίζει τον τελικό βαθμό του μαθήματος, ο οποίος είναι άθροισμα του 30% του προφορικού βαθμού και του 70% του γραπτού βαθμού. Επίσης, να εμφανίζει το ονοματεπώνυμο του μαθητή και τον τελικό βαθμό του μαθήματος.
Β2.4. Να υπολογίζει και να εμφανίζει το πλήθος των μαθητών που έχουν βαθμό μεγαλύτερο του 18.
"""
exit = False
ano18 = 0
while not exit:
    name = raw_input("ONOMA MATHITH: ").upper()
    # έξοδος με κενό ή space
    if name == "" or name == " ":
        print "BYE"
        exit = True
    else:
        vathPro = input("PROFORIKOS VATHMOS: ")
        # while για όσες φορές δωθεί λάθος βαθμός
        while vathPro not in range(0, 21):
            print "LATHOS BATHMOS"
            vathPro = input("PROFORIKOS VATHMOS: ")

        vathGra = input("GRAPTOS VATHMOS: ")
        # while για όσες φορές δωθεί λάθος βαθμός
        while vathGra not in range(0, 21):
            print "LATHOS VATHMOS: "
            vathGra = input("GRAPTOS VATHMOS: ")

        sum = (vathPro*0.3) + (vathGra*0.7)
        if sum > 18:
            ano18 += 1
            
        print "O", name, "EXEI TELIKO VATHMO: ", sum
        print "SYNOLO MATHINON ANO 18: ", ano18
        

    
