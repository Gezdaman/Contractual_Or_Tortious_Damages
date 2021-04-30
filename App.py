x = input("What was the price of the good/service/business purchased?")
print("The price of the good/service/business purchased was " + str(x))

y = input("What was the warranted value of the good/service/business purchased, according to the purchase contract?")
print("The warranted value of the good/service/business purchase was " + str(y))

z = input("What is the actual value of the good/service/business purchased?")
print("The actual value of the good/service/business purchased is " + str(z))

if (x-z) > (y-x):
    print("You should claim on a tortious basis, pursuant to a pre-contractual misrepresentation(s).")

if (y-x) > (x-z):
    print("You should claim on a contractual basis, pursuant to the representation or warranty made in the purchase contract.")

elif (y-x) == (x-z):
    print("Both the tortious measure and the contractual measure are equally advantageous.")
