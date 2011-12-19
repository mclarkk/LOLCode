#Author: Meghan Clark
#A (very short) text adventure written with no loops or if statements.
#Control flow is done entirely with try-except blocks and recursion.

import os

cardinalDirections = {"north":0, "south":1, "east":2, "west":3}
booleans = {"n":0, False: 0, "y":1, True: 1}
osNames = ["posix", ("nt", "dos", "ce")]
osNum = None

def main():
	gameRound()

def gameRound():
	startMessage = "You find yourself standing in a field. Which way do you want to go?\n"
	northMessage = "\nDeath by tornado! You've been blown away."
	southMessage = "\nDeath by earthquake! You're no longer grounded in this reality."
	eastMessage = "\nDeath by volcano! The fire has gone from your spirit."
	westMessage = "\nDeath by tsunami! A peaceful calm washes over you. So do the waves."
	direction = ""
	repeat = ""

	#clear screen
	try:
		1/osNames.index(os.name)
	except ZeroDivisionError:
		os.system('clear')
	except ValueError:
		try:
			1/(booleans[os.name in osNames[1]])
		except ZeroDivisionError:
			os.system('CLS')
		else:
			print '\n' * 100

	#begin game
	print startMessage
	input = raw_input("I go (North/South/East/West): ")

	try:
		cardinalDirections[input.lower()]
	except KeyError:
		direction = tryDirectionAgain()
	else:
		direction = input.lower()

	try:
		1/cardinalDirections[direction]
	except ZeroDivisionError:
		print northMessage

	try:
		1/(cardinalDirections[direction]-1)
	except ZeroDivisionError:
		print southMessage

	try:
		1/(cardinalDirections[direction]-2)
	except ZeroDivisionError:
		print eastMessage

	try:
		1/(cardinalDirections[direction]-3)
	except ZeroDivisionError:
		print westMessage

	input = raw_input("\nPlay again? (y/n): ")
	
	try:
		booleans[input.lower()]
	except KeyError:
		repeat = tryRepeatAgain()
	else:
		repeat = input.lower()

	try:
		1/(booleans[repeat]-1)
	except:
		gameRound()

#recurses until it gets valid input
def tryDirectionAgain():
	input = raw_input("Sorry, you can't go that way. Try again: ")
	try:
		cardinalDirections[input.lower()]
		return input.lower()
	except KeyError:
		return tryDirectionAgain()	

#recurses until it gets valid input
def tryRepeatAgain():
	input = raw_input("Please type 'y' or 'n': ")
	try:
		booleans[input.lower()]
		return input.lower()
	except KeyError:
		return tryRepeatAgain()	

main()
	
