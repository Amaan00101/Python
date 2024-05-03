# dictionary methods 1 exercises

# create a variable and assign it the following dictionary:
# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
new_dict = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}

# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.
new_dict = {"Queen": "Bohemian Rhapsody", 
            "Bee Gees": "Stayin' Alive", 
            "U2": "One", 
            "Michael Jackson": "Billie Jean", 
            "The Beatles": "Hey Jude", 
            "Bob Dylan": "Like A Rolling Stone"
}


# print the length of the dictionary.
print(len(new_dict))

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for new in new_dict.keys():
    print(new)

# print all of the values from the dictionary using the .values() method.
print(new_dict.values())

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key, value in new_dict.items():
    print(key, value)

# use the .get() method to check the dictionary for the key "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

print(new_dict.get("Promise of the Real", "The key is not found in the dictionary."))