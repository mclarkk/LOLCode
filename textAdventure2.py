#Author: Meghan Clark
#A (very short) text adventure written with no loops or if statements.
#Control flow is done entirely with try-except blocks and recursion.

import os as ____________

_ = {"north":0, "south":1, "east":2, "west":3}
__ = {"n":0, False: 0, "y":1, True: 1}
___ = ["posix", ("nt", "dos", "ce")]
____ = None

def main():
	______________()

def ______________():
	_____ = "You find yourself standing in a field. Which way do you want to go?\n"
	______ = "\nDeath by tornado! You've been blown away."
	_______ = "\nDeath by earthquake! You're no longer grounded in this reality."
	________ = "\nDeath by volcano! The fire has gone from your spirit."
	_________ = "\nDeath by tsunami! A peaceful calm washes over you. So do the waves."
	__________ = ""
	___________ = ""

	#clear screen
	try:
		1/___.index(____________.name)
	except ZeroDivisionError:
		____________.system('clear')
	except ValueError:
		try:
			1/(__[____________.name in ___[1]])
			print '\n' * 100
		except ZeroDivisionError:
			____________.system('CLS')

	#begin game
	print _____
	_____________ = raw_input("I go (North/South/East/West): ")

	try:
		_[_____________.lower()]
		__________ = _____________.lower()
	except KeyError:
		__________ = _______________()

	try:
		1/_[__________]
	except ZeroDivisionError:
		print ______

	try:
		1/(_[__________]-1)
	except ZeroDivisionError:
		print _______

	try:
		1/(_[__________]-2)
	except ZeroDivisionError:
		print ________

	try:
		1/(_[__________]-3)
	except ZeroDivisionError:
		print _________

	_____________ = raw_input("\nPlay again? (y/n): ")
	
	try:
		__[_____________.lower()]
		___________ = _____________.lower()
	except KeyError:
		___________ = ________________()

	try:
		1/(__[___________]-1)
	except:
		______________()

#recurses until it gets valid _____________
def _______________():
	_____________ = raw_input("Sorry, you can't go that way. Try again: ")
	try:
		_[_____________.lower()]
		return _____________.lower()
	except KeyError:
		return _______________()	

#recurses until it gets valid _____________
def ________________():
	_____________ = raw_input("Please type 'y' or 'n': ")
	try:
		__[_____________.lower()]
		return _____________.lower()
	except KeyError:
		return ________________()	

main()
	
