x = input("What was the price of the good/service/business purchased?")
print("The price of the good/service/business purchased was " + str(x))

y = input("What was the represented value of the good/service/business purchased, according to the purchase contract?")
print("The represented value of the good/service/business purchase was " + str(y))

z = input("What is the actual value of the good/service/business purchased?")
print("The actual value of the good/service/business purchased is " + str(z))

if x >= z:
    print("You should claim on a tortious basis, pursuant to a pre-contractual misrepresentation(s).")

if y >= z:
    print("You should claim on a contractual basis, pursuant to the representation or warranty made in the purchase contract.")