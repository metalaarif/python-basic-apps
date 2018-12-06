'''

It will give us random order or print random order
'''

symbol_to_name ={"H": "hydrogen", # key / value
                 "He": "Helium",
                 "Li": "Lithium",
                 "C": "Carbon",
                 "O": "Oxygen",
                 "N": "Nitrogen"
                 }
print(symbol_to_name)

print(symbol_to_name.get("O"))

print(len(symbol_to_name))
print(symbol_to_name.keys())    # prints all the keys
print(symbol_to_name.values())  # prints all the values
print(symbol_to_name.items())   # prints full list with key and values within tuples

symbol_to_name.update({"Mg": "Magnesium", "Ag": "Gold"}) # updates adds keys and values
print(symbol_to_name)

print(symbol_to_name["He"])     # prints only He value "Helium"

symbol_to_name.update({"Mg": "Maganesium"})
print(symbol_to_name)           # duplicates keys are values are replaced.

symbol_to_name["Mg"]="Magnesium"
print(symbol_to_name)

del symbol_to_name["Mg"]
print(symbol_to_name)

for k, v  in symbol_to_name.items():
    print("Keys is %s added value is %s" %(k, v))

