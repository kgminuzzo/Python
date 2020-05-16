fruits = ["apple","orange","pear","grapes"]

#for fruit in fruits:
#    print("Would you like {}?".format(fruit))

for number in range(1,11):
    if number == 7:
        print("We are skipping the 7")
        continue
    if number == 9:
        pass
    else:
        print("Number {}".format(number))

    print("Next...")

temp = 45
while temp > 30:
    print("The water temp is {}".format(temp))
    temp -=1
    if temp == 33:
        break