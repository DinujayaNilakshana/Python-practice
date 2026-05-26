Distance = float(input("Distance Travelled?"))
Fuel_Efficiency = float(input("Fuel economy?"))
Highway_charge = float(input("Highway charge?"))
Fuel_PPL = float(input("Fuel PPL?"))

Fuel_Used= Distance / Fuel_Efficiency

Fuel_cost = Fuel_Used * Fuel_PPL

Total = Fuel_cost + Highway_charge

print("Amount of Fuel Consumed", Fuel_Used)
print("Cost For The Fuel", Fuel_cost)
print("Total Cost Of Your Trip is", Total)

