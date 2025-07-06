# {key : value}
# No duplicates

capitals = {"USA" : "Washington DC",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Russia"):
    print("Capital does exists")
else:
    print("This capital does not exists")
    
capitals.update({"Germany" : "berlin"})
print(capitals)
capitals.update({"USA" : "Detroit"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.popitem()
print(capitals)

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key} : {value}")

# capitals.clear()
# print(capitals)
