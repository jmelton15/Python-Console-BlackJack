import random
import math
import blackjackMoney
import colorama
from colorama import Fore, Back, Style

colorama.init()


suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}




class Card:
	'''
	Class that wil be used to create cards
	assigning suits to each card rank/value
	'''

	def __init__(self,suit,rank):

		self.suit = suit
		self.rank = rank
		#self.value = value


	def __str__(self):

		return (f"{self.rank} of {self.suit}") 


class Deck():
	'''
	Class that will be used to create a full deck of cards
	'''


	def __init__(self):

		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))


	def __str__(self):
		'''
		This Method can be used to test that all the cards are being created 
		and appearing in the deck correctly
		'''

		testString = ''

		for card in self.deck:
			testString += '\n ' + card.__str__()
		return 'The Deck Has: ' + testString

	def shuffle(self):
		'''
		This method shuffles the deck and stores it in
		a new list called SD
		'''
		random.shuffle(self.deck)



class Hand():

	def __init__(self):
		self.cards = []
		self.initialPlayerHandValue = 0
		self.initialCompHandValue = 0
		self.playerValueStoreList = []
		self.compValueStoreList = []
		self.pAces = 0
		self.cAces = 0
		self.computerHand = []
		self.playerHand = []
		self.pHand = []
		self.cHand = []
		self.playerRunningTotal = 0
		self.compRunningTotal = 0
		self.usedAces = 0

		#self.pHandSuit = ''

		self.firstDeck = Deck()
		self.firstDeck.shuffle()


	def deal(self):
		'''
		This method deals the cards out blackjack style
		to create an initial two card hand for both player and computer
		'''
		
		pHandString = ''
		cHandString = ''
		i = 0

		#this while loop should give each the player
		#and the computer two cards in their hands
		while i < 2:
			self.playerHand.append(self.firstDeck.deck.pop()) 
			self.computerHand.append(self.firstDeck.deck.pop())
			i += 1



		#this will turn the list values into a tuple called bothHands so we can return the initial hands
		#as one object
		bothHands = (self.playerHand[0],self.playerHand[1],self.computerHand[0],self.computerHand[1])
		

		#This code turns the list values into strings for printing
		pHandString = str(self.playerHand[0]) + str(self.playerHand[1])
		cHandString = str(self.playerHand[0]) + str(self.playerHand[1])

		#use this lines to test the hands
		#print('Players Hand is: {} \nComputer Hand is: {}'.format(pHandString,cHandString))
		#return bothHands



	def add_player_hand(self,hand):
		
		if len(self.playerValueStoreList) == 0:

			self.initialPlayerHandValue = values[hand[0].rank] + values[hand[1].rank]

			#This checks the initial hand for any ACE cards
			self.pHand = [hand[0].rank,hand[1].rank] 

			#here we create a list that stores all the values of the cards 
			#this will be used later to add new cards from HIT method and add those new values
			self.playerValueStoreList = [values[hand[0].rank],values[hand[1].rank]]

			for card in self.pHand:
				if card == 'Ace':
					self.pAces += 1

		else:
			#This loop will add any new cards added from the HIT method to the store list
			for card in hand[(len(hand))-1:]:
				self.playerValueStoreList.append(values[card.rank])

			for card in hand[(len(hand))-1:]:
				self.pHand.append(card.rank)


			for card in self.pHand:
				if card == 'Ace':
					self.pAces += 1

		self.playerRunningTotal = sum(self.playerValueStoreList)

		#self.pHandSuit = hand[0].suit


	def add_computer_hand(self,hand):

		if len(self.compValueStoreList) == 0:

			self.initialCompHandValue = values[hand[0].rank] + values[hand[1].rank]

			#This checks the initial hand for any ACE cards
			self.cHand = [hand[0].rank,hand[1].rank] 

			#here we create a list that stores all the values of the cards 
			#this will be used later to add new cards from HIT method and add those new values
			self.compValueStoreList = [values[hand[0].rank],values[hand[1].rank]]

			for card in self.cHand:
				if card == 'Ace':
					self.cAces += 1

		else:
			#This loop will add any new cards added from the HIT method to the store list
			for card in hand[(len(hand))-1:]:
				self.compValueStoreList.append(values[card.rank])

	
			for card in hand[(len(hand))-1:]:
				self.cHand.append(card.rank)


			for card in self.cHand:
				if card == 'Ace':
					self.cAces += 1

		self.compRunningTotal = sum(self.compValueStoreList)

	def hit(self,hand):

		hand.append(self.firstDeck.deck.pop())
		#return hand

	def adjust_for_player_ace(self,total,aces):
		adjust = ''
		amount = 0
		second = ''
		goSecond = True

		while True:
			try:
				if aces > 0 and self.usedAces == 0:
					adjust = input("You have {} Aces. Would you like to adjust one or more of them from 11 to 1?\n".format(aces))
				elif self.usedAces ==2:
					second = input("You have changed {} Aces Already, but you now have {} Aces. Would you like to adjust the second one from 11 to 1?\n".format(self.usedAces,aces))
				else:
					print(Fore.BLACK + Back.WHITE)
					print("You dont have any Aces")
					print("\nYour Hand Value Is: {}  ".format(total))
					print(Style.RESET_ALL)
					#return total
					break
			except:
				print("Your response must be y, n, yes, or no. Please try again")
				continue
			else:
				if adjust.upper() == 'Y' or adjust.upper() == 'YES':
					try:
						amount = int(input("How many of your {} Aces would you like to change?".format(aces)))
					except:
						print("Your response must be a number. Please try again")
						continue
					else:
						self.playerRunningTotal = total - (10*amount)
						self.usedAces += 1
						print("Your new Hand Value is: {}".format(self.playerRunningTotal))
						break
				if adjust.upper() == 'N' or adjust.upper() == 'NO':
					print(Fore.BLACK + Back.WHITE)
					print("\nYour Hand Value Is: {}".format(total))
					print(Style.RESET_ALL)
					#return total
					break



	def adjust_for_computer_ace(self,total,aces):
		adjust = ''
		amount = 0
		while True:
			try:
				if aces > 0:
					adjust = input("You have {} Aces. Would you like to adjust one or more of them from 11 to 1?\n".format(aces))
				else:
					print("You dont have any Aces")
					print("\nYour Hand Value Is: {}".format(total))
					#return total
					break
			except:
				print("Your resposne must be y, n, yes, or no. Please try again")
				continue
			else:
				if adjust.upper() == 'Y' or adjust.upper() == 'YES':
					try:
						amount = int(input("How many of your {} Aces would you like to adjust?".format(aces)))
					except:
						print("Your response must be a number. Please try again")
						continue
					else:
						self.compRunningTotal = total - (10*amount)
						print(Fore.BLACK + Back.WHITE)
						print("Your new Hand Value is: {}".format(self.compRunningTotal))
						#return total
						break
				if adjust.upper() == 'N' or adjust.upper() == 'NO':
					print("\nYour Hand Value Is: {}".format(total))
					#return total
					break


def show_some_cards(pHand,cHand):
	print(Back.RED + Style.BRIGHT)
	print("\n\nDealers Hand:   ")
	print("\n\n*Hidden Card*  ")
	print(" ",str(cHand[1]) + "  ")
	print(Style.RESET_ALL)
	print(Back.CYAN + Style.BRIGHT)
	print("\nYour Hand: ")
	print("\n")
	for card in pHand:
		print("",str(card))
	print(Style.RESET_ALL)
	

def show_all_cards(pHand,cHand):
	print(Back.RED + Style.BRIGHT)
	print("\n\nDealer's Hand: ")
	print("\n")
	for card in cHand:
		print(" ",str(card) + "  ")
	print(Style.RESET_ALL)
	print(Back.CYAN + Style.BRIGHT)
	print("\nYour Hand: ")
	print("\n")
	for card in pHand:
		print(" ",str(card) + "  ")
	print(Style.RESET_ALL)
	





































		








