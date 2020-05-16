stuff = {"food": 15, "energy": 100, "enemies":3}
print(stuff.get("food"))
print(stuff.items())
print(stuff.keys())
print(stuff.values())
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)
print(stuff.popitem())
print(stuff)
print(stuff.pop("food"))
print(stuff)

new_items = {"rocks":32,"arrows":43}
stuff.update(new_items)
print(stuff)