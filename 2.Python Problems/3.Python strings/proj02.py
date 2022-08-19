
# purchase price and payment will be kept in cents

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("Welcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))


while in_str != 'q':
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: \n")
        if in_str<0:
                print("Value can not be negative")
                continue
        
        in_str = round(in_str)
        print("Input dollars paid:",in_str)
        

        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: \n")
