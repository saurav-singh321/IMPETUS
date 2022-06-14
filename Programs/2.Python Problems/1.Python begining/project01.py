input_rods = float(input("Input rods: "))
input_rods = input_rods
meters = round(5.0292*input_rods, 3)
furlong = round(0.025*input_rods, 3)
miles = round(0.00312*input_rods, 3)
feet = round(16.50003*input_rods, 3)
print(f"You input {input_rods} rods.\nConversions\nMeters: {meters}\nFeet: {feet}\nMiles: {miles}\nFurlongs: {furlong}")
