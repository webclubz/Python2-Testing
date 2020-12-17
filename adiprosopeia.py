# -*- coding: utf-8 -*-
"""
Σε μία αντιπροσωπεία αυτοκινήτων αποφασίστηκε, για κάθε πελάτη που αγοράζει αυτοκίνητο να γίνεται κλιμακωτή έκπτωση ανάλογα με την τιμή του αυτοκινήτου, με βάση τον πίνακα.

έως και 10.000€ -> 4%
πάνω από 10.000 € έως και 14.000 ->7% 
€ πάνω από 14.000 €    10%

Να υλοποιήσετε πρόγραμμα το οποίο:
α.	Για κάθε πελάτη που αγοράζει αυτοκίνητο:
1.	διαβάζει το όνομά του και την τιμή του αυτοκινήτου που αγόρασε,
2.	καλεί συνάρτηση που δέχεται την τιμή του αυτοκινήτου και επιστρέφει την έκπτωση που του αντιστοιχεί,
3.	εμφανίζει το όνομά του και το ποσό που θα πληρώσει μετά την έκπτωση.
β.	Να επαναλαμβάνει τα παραπάνω, μέχρι να δοθεί ως όνομα πελάτη η λέξη
«TELOS».
γ.	Να εμφανίζει μετά το τέλος της επανάληψης:
1.	τη συνολική έκπτωση πουέγινε για όλους τους πελάτες,
2.	το πλήθος των πελατών που αγόρασαν αυτοκίνητα άνω των 14.000 €.
"""
print "================================"
print "Use exit to escape"
print "================================"


def disc(price):

    if (price <= 10000):
        disc = price * 0.04
    elif (price <= 14000):
        disc = 10000 * 0.04 + (price - 10000) * 0.07
    else:
        disc = 10000 * 0.04 + 4000 * 0.07 (price - 14000) * 0.10
    
    return disc

####################################

customersSum = 0; discountSum = 0; customersLarge = 0

while True: 
    name = raw_input("ONOMA PELATH: ")
    if (name == "exit"):
        print "================================="
        break
    price = input("TIMH AYTOKINHTOY: ")
    if (price > 14000):
        customersLarge += 1

    discount = disc(price)  # ΕΚΠΤΩΣΗ
    finalPrice = price - discount # ΤΙΜΕ ΜΕ ΕΚΠΤΩΣΗ
    
    # ΣΥΝΟΛΑ
    customersSum += 1 
    discountSum += discount  

    print "EKPTOSH: ", discount, "EURO"
    print "ONOMA PELATH: ", name
    print "TELIKO POSO PLHROMHS: ", finalPrice, "EURO"
    print "=====================================" 

print "SYNOLO EKPTOSHS: ", discountSum, "EURO"
print "SYNOLIKOI PELATES: ", customersSum
print "SYNOLIKOI FRAGATOI PELATES: ", customersLarge
print "Bye :)"

  
