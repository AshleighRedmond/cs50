
# n = int(input("Number: "))

# if n > 0:
# 	print("n is positive")
# elif n < 0:
# 	print("n is negative")
# else:
# 	print("n is zero")




# name = "Harry"

# print(name[0])


# names = ["Harry", "Ron", "Hermione"]

# print(names[1][2])

# /tuple/
# coordinate = (10.0, 20.0)

# Define a list of names
# names = ["Harry", "Ron", "Hermione", "Ginny"]

# names.append("Draco")
# names.sort()
# print(names)

# #Set
# s = set()

# #Add elements
# s.add(1)
# s.add(2)
# print(s)

# print(f"This set has {len(s)} elements")

# for i in range(6):
# 	print(i)

# houses = {"Harry":"Gryffindor", "Draco":"Slytherin"}
# houses["Hermione"] = "Gryffindor"

# print(houses["Harry"])

# /functions/

# def square(x):
# 	return x * x

# for i in range(10):
# 	print(f"The square of {i} is {square(i)}")

# /classes/

# class Point():
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# p = Point(2, 8)

# print(p.x)
# print(p.y)

# class Flight():
# 	def __init__(self, capacity):
# 		self.capacity = capacity
# 		self.passengers = []

# 	def add_passenger(self, name):
# 		if not self.open_seats():
# 			return False
# 		self.passengers.append(name)
# 		return True

# 	def open_seats(self):
# 		return self.capacity - len(self.passengers)


# flight = Flight(3)

# names = ["Harry", "Ron", "Hermione", "Ginny"]

# for name in names:
# 	if flight.add_passenger(name):
# 		print(f"Added {name} to flight successfully")
# 	else:
# 		print(f"No available seats for {name}")

# /decorators/

# def announce(f):
# 	def wrapper():
# 		print("About to run the function...")
# 		f()
# 		print("Done with the function.")
# 	return wrapper()

# @announce
# def hello():
# 	print("Hello, world!")

# /lambda/

# people = [
# 	{"name": "Harry", "house": "Gryffindor"},
# 	{"name": "Cho", "house": "Ravenclaw"},
# 	{"name": "Draco", "house": "Slytherin"}
# ]

# # def f(person):
# # 	return person["name"]

# # people.sort(key=f)
# people.sort(key=lambda person: person["name"])

# print(people)


# /error handling/
import sys

try:
	x = int(input("x: "))
	y = int(input("y: "))
except ValueError:
	print("Error: Invalid input")
	sys.exit(1)

try:
	result = x / y
except ZeroDivisionError:
		print("Error: Cannot divide by 0.")
		sys.exit(1)

print(f"{x} / {y} = {result}")




















