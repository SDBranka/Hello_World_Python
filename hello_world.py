# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
print("\n\n---#2---")
name = "Noelle"
print("Hello", name)	# with a comma
print( "Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
print("\n\n---#3---")
name = 42
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
print("\n\n---#4---")
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

print("\n\n---.title()---")
name = "elizabeth taylor"
print(name.title())  #prints first letter of each word as uppercase without changing value
print(name)

print("\n\n---.split()---")
x = name.split(" ")  #splits string at designate character (if no value entered splits between each char)
print(x)
print(name)

print("\n\n---.join()---")
a_list = ["h", "e", "l", "l", "o"]
x = "".join(a_list)
print(x)
y = " ".join(a_list)
print(y)
z = "&".join(a_list)
print(z)

