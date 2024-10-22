print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")


print("\n\n---- Day 1 -----")

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a " + "\\" +" and the letter n")
print("\n\n")

print("------ Third Glass Exercise ------")
glass1 = "milk"
glass2 = "juice"
glass3 = glass1
glass1 = glass2
glass2 = glass3
print("We have 2 variables glass1 and glass2.")
print("glass1 contains " + glass2 + " and glass2 contains "+ glass1+ ".")
print("----------------------------------")

print("\n\n\n----- Brnad Name Generator -----")
print("Welcome to the brand name generator game! ")
city = input("What is the name of the city you grow up in? ")
pet = input("What is the name of a pet? ")
print("Your brand name could be : " + city +" "+ pet)




print("Hello, "+ input("What is your name?"))
'''
What is your name?Angela
Hello, Angela
'''

name1 = "Angela"
print(name1)
name2 = "Yu"
print(name2)

username = input("What is your name?")
length = len(username)
print("Your user name : " + username)
print(f"Length : {length}")