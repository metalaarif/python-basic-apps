name = {
    "Apple": ("Sweet", "Green and Red", "Edible"),
    "Mango": ("Sweet", "Yellow and Green", "Edible"),
    "Grapes": ("Sweet", "Green and Red and Black", "Edible"),
    "Dragonfruit": ("Sweet", "Pink", "Edible"),
    "Danger Berry": ("Tangy", "Black", "Poisonous"),
    "PoisonIvy": ("Bitter", "Ember", "Poisonous")
}

for x in name.values():
    print(x[1])
    # print("{} is {} and it is {}".format(x[1], x[1], x[1]))