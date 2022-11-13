from random import randint

def get_temperature(senser):
    return randint(-20,0) if senser else randint(0,20)

def get_pressure(senser):
    if senser:
        return randint(720,750)  
    else:
         return randint(750,770)

def get_wind_speed(senser):
    if senser == 1:
        return randint(0,30)
    else:
        return randint(30,50)

def data_collection(senser = 1):
    return (get_temperature(senser),get_pressure(senser),get_wind_speed(senser))

   