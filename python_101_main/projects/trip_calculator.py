# a trip cost calculator

distance = 100 #int(input("Enter travel distance in kilometers: "))
kpl = 30 #int(input("Enter kilometers per liter: "))
price = 5 #int(input("Enter price per liter: "))

cost = ((distance / kpl) * price)

print(f"It will cost ${cost} to take this trip.")