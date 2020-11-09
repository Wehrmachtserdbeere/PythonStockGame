import random
print("Stock Game\nBy Strawberry Software\n\n-------------------------------------------------------------------------")
stocks = 0
amo = 1
while True:
    r = random.random()
    if r >= 0.5:
        stocks += random.random()*10 * amo
    elif r <= 0.5:
        stocks -= random.random()*10 * amo
    print("Stocks are at " + str(stocks) + " points")
    inp = input("Invest (yes/no)? ")
    if inp == "no":
        break
    elif inp == "yes":
        amo = int(input("How much do you want to invest (Numbers only)? "))
        pass
    else:
        print("Not a valid response.")
print("You exited with Stocks at " + str(stocks) + " points")
i = input("Press Enter to exit.")
quit()
