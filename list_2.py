# del and list methods exercises

# Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animal = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Use del to remove "tiger" from the list assigned to arctic_animals.
del arctic_animal[4]

# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
arctic_animal.remove("elephant")

# Use the .append() method to add the string "arctic fox" to the list arctic_animals.
arctic_animal.append("arctic fox")

# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
arctic_animal.insert(2, "snowy owl")

# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
arctic_animal.sort()

# Use print() to display the list assigned to arctic_animals
print(arctic_animal)

# Use .index() to get the index number of "reindeer" from arctic_animals then print it.
print(arctic_animal.index("reindeer"))

# Use .pop() to get the last item from the list arctic_animals then print it.
print(arctic_animal.pop())