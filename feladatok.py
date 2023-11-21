"""1-	Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!"""
def feladat1():
    print("1. Feladat")
    db: int= 0
    for i in range(1, 1001, 1):
        if i % 7 == 0:
            db += 1
    return db


"""2-	Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!"""
def feladat2():
    print("2. Feladat")
    db: int= 0
    for i in range(2000, 20001, 1):
        if i % 12 == 0:
            db += 1
    return db


"""3-	Írd ki az első 20 3-mal osztható szám négyzetének összegét!"""
def feladat3():
    print("3. Feladat")
    szam: int= 0
    osszeg: int= 0
    negyzet: int= 0
    while negyzet < 20:
        if szam % 3 == 0:
            osszeg += szam **2 
            negyzet += 1
        szam += 1
    return osszeg


"""4-	Keresd meg egy szám egész osztóit!"""
def feladat4(a:int):
    print("4. Feladat")
    szam: int= 0
    for i in range(1, a + 1):
        if a % i == 0:
            szam += 1
    return szam


"""5-	Keresd meg egy szám legnagyobb egész osztóját!"""
def feladat5(a:int):
    print("5. Feladat")
    i:int = 0
    while i > 1:
        if a % i == 0:
            i -= 1
    return a
