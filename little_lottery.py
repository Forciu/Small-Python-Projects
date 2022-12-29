from pdb import Restart
import random

try:
    Howmany = int(input("Enter the number of bet: "))
    Maxnumber = int(input("Enter the maximum random number: "))
    if Howmany > Maxnumber:
        print("The given number is larger than the options, I recommend 2x more")
        exit()
except ValueError:
    print("Incorrect data..")
    exit()

numbers = []
i = 0
while i < Howmany:
    number = random.randint(1, Maxnumber)
    if numbers.count(number) == 0:
        numbers.append(number)
        i = i + 1

for i in range(2):
    print("Choose %s from %s numbers: " % (Howmany, Maxnumber))

    types = set()
    i = 0
    while i < Howmany:
        try:
            typ = int(input("Enter the numbers %s: " % ( i +1)))
        except ValueError:
            print("Incorrect data..")
            continue

        if 0 < typ <= Maxnumber and typ not in types:
            types.add(typ)
            i = i + 1
        if typ > Maxnumber:
            print("You cannot select numbers larger than the field.. Let's start again")
            op = input("Again (t/n)? ")
            if op == "t":
                Restart
            else:
                exit()

    hit = set(numbers) & types
    if hit:
        print("\nNumber of hits: %s " % len(hit))
        print("Your hit numbers: ", hit)
    else:
        print("No hits..")
    print("\n" + "x" * 40 + "\n")
print("Drawn numbers: ", numbers)