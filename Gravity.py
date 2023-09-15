import datetime, math
G=6.6743*math.pow(10,-11)
Em=5.97600*math.pow(10,24)
Dopmass=(datetime.date(2023,9,1)-datetime.date(2005,6,30)).days
Dopdistance=100000*math.pow(10,3)

def Grav(m,r):
    return (G*Em)*(m/math.pow(r,2))

def Masscon(mn):
    if "kg" in mn:
        return float(mn[0:mn.find("^")-3])*pow(10,int(mn[mn.find("^")+1:]))
    elif "Mt" in mn:
        return float(mn[0:mn.find("^")-3])*pow(10,int(mn[mn.find("^")+1:]))*pow(10,9)
    elif "Gt" in mn:
        return float(mn[0:mn.find("^")-3])*pow(10,int(mn[mn.find("^")+1:]))*pow(10,12)
    elif "t" in mn:
        return float(mn[0:mn.find("^")-2])*pow(10,int(mn[mn.find("^")+1:]))*pow(10,3)
    else:
        return mn

def Lencon(ln):
    if "km" in ln:
        return float(ln[0:ln.find("^")-3])*pow(10,int(ln[ln.find("^")+1:]))*pow(10,3)
    elif "m" in ln:
        return float(ln[0:ln.find("^")-3])*pow(10,int(ln[ln.find("^")+1:]))
    else:
        return ln

mm=input("Write Down Planet's Mass With Measurements (kg, t, Mt, Gt) And '^' To Show Power of 10 (10 kg^2 = 10*10^2). Use Dots and No Commas ")
mr=input("Write Down Distance To Said Planet With Measurements (m, km). Use Dots and No Commas ")

print("Answer for main Task: ", str(Grav(Masscon(mm),Lencon(mr))), "N")
print("Answer for side Task: ", str(Grav(int(str(Dopmass))*math.pow(10,3),int(Dopdistance))))