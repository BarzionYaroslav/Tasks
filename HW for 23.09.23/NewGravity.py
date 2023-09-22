import datetime, math
G=6.6743*math.pow(10,-11)
Em=5.97600*math.pow(10,24)
Dopmass=(datetime.date(2023,9,1)-datetime.date(2005,6,30)).days
Dopdistance=100000*math.pow(10,3)

def Grav(m,r):
    return (G*Em)*(m/math.pow(r,2))

print("Притяжение к Меркурию "+str(Grav(Em*0.055,149650000000)))
print("Притяжение к Венере "+str(Grav(Em*0.815,149500000000)))
print("Притяжение к Марсу "+str(Grav(Em*0.107,227800000000)))
print("Притяжение к Юпитеру "+str(Grav(Em*318,778000000000)))
print("Притяжение к Сатурну "+str(Grav(Em*95.2,1400000000000)))
print("Притяжение к Урану "+str(Grav(Em*14.6,2800000000000)))
print("Притяжение к Нептуну "+str(Grav(Em*17.2,4500000000000)))