#!/usr/bin/env python3

# #class attributes are attributes specific to the class not the instance to the object of that class

# class Person:
# 	#this is a class attribute not a regular attribute because it does not use self
# 	number_of_people = 0

# 	def __init__(self, name):
# 		self.name = name
# 		Person.add_person()

# #class methods act on the class itself not any instance, that's why cls is written instead
# 	@classmethod
# 	def number_of_people_(cls):
# 		return cls.number_of_people

# 	@classmethod
# 	def add_person(cls):
# 		cls.number_of_people += 1		

# p1 = Person("tim")

# p2 = Person("jill")

# print(Person.number_of_people_())



#static methods are for when you want to create classes that organize functions
#static methods do not access to an instance just like class methods
#

class Math:

	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def pr():
		print("run")

print(Math.pr())

#everything we work with in python is an object