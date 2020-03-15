# -*- coding: utf-8 -*-

def lines():
    print
    print "--------------------------"
    print

lines()
# TIMES
prices = {
    "a" : "1.90",
    "m" : "1.30",
    "f" : "4.80",
    "fBig" : "6.70"
}

# METRITES
ac = 0; fc = 0; fbc = 0; mc = 0

# INFO MESSAGE
warnMsg = "Epitrepomenes Times\n\na = aytokinhto\nf = Fortigo\nm = Moto".upper()
print warnMsg
lines()

# LOOP
while True :
    lines()
    vType = raw_input("Eisagogh typou oxhmatos :".upper())
    lines()
    if vType == "a":
        aPrice = float(prices["a"])
        print "Aytokinito\nTimh :".upper(), aPrice
        ac += 1
        aSum = ac * aPrice

    elif vType == "f":
        fType = int(raw_input("Mhkos Forthgou? : ".upper()))
        if fType <= 5:
            fPrice = float(prices["f"])
            print "Fortigo <= 5\nTimh :".upper(), fPrice
            fc += 1
            fSum = fc * fPrice
        else :
            fbPrice = float(prices["fBig"])
            print "Fortigo > 5m\nTimh :".upper(), fbPrice
            fbc += 1
            fbSum = fbc * fbPrice

    elif vType == "m":
        mPrice = float(prices["m"])
        print "Moto\nTimh :".upper(), mPrice
        mc += 1
        mSum = mc * mPrice

    else:
        if vType == "report":
            print "Aytokinita :", ac, "| Synolo : ", aSum
            print "Fortiga Mikra :", fc, "| Synolo : ", fSum
            print "Fortiga Megala :", fbc, "| Synolo : ", fbSum
            print "Moto", mc, "| Synolo : ", mSum
            print
            print "Synolo Oxhmaton : ", ac + fc + fbc + mc  
            print "Synolo Eisprakseon : ", aSum + fSum + fbSum + mSum  

        elif vType == "exit":
            print "End of program ##### Bye :)".upper()
            break
        else :
            lines()
            print "SFALMA!\n", warnMsg

