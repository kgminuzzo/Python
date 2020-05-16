fruits = ["apple","orange","pear","grapes"]
colors = ["green","blue",213,3.4]

print(fruits, colors)
fruits.append("banana")
print(fruits)
fruits.extend(colors)
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.pop(3)
print(fruits)
fruits.pop(-1)
print(fruits)
#fruits.sort()
#print(fruits)
print("orange" in fruits)
print(fruits.count("apple"))
print(fruits.index("apple"))