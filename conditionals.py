name = input("Whats your name? ")
if name.startswith("Kari"):
    print("Hi {}!".format(name))
elif name == "Karina":#this is not going to be executed
    print("Hi {} nice to have you here!".format(name))
elif name =="Danielle":
    print("Hi {}!".format(name))
else:
    print("Hi stranger!")
print("Have a nice day!")