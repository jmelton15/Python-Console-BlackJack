import colorama
from colorama import Fore, Back, Style

class Chips:

	def __init__(self):
		self.total = 50
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

	def blackjack(self):
		self.total += (self.bet + (self.bet*.5))

def bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Your bet can only be a number. Please try again!")
			continue
		else:
			if chips.bet > chips.total:
				print("Your bet cannot exceed your budget", chips.total)
			else:
				print("Bets have been placed!")
				break
			
def player_busts(pHand,cHand,chips):
	print(Style.BRIGHT + "You bust!")
	chips.lose_bet()
	

def player_wins(pHand,cHand,chips):
	print(Style.BRIGHT + "You Win!")
	chips.win_bet()
	

def dealer_busts(pHand, cHand, chips):
	print(Style.RESET_ALL)
	print(Style.BRIGHT + "Dealer Busts! You Win!")
	chips.win_bet()
	

def dealer_wins(pHand,cHand,chips):
	print(Style.BRIGHT + "Dealer Wins!")
	chips.lose_bet()
	

def push(pHand,cHand):
	print(Style.BRIGHT + "Hands tied. It's a push!")
	

def player_blackjack(pHand,cHand,chips):
	print(Style.BRIGHT + "You got Natural BlackJack! Congratulations!")
	chips.blackjack()
	

def dealer_blackjack(pHand,cHand,chips):
	print(Style.BRIGHT + "Dealer got 21, You Lose! Better Luck Next Time!")
	chips.lose_bet()

def chipless(chips):
	if chips == 0:
		return True
	else:
		return False
	





	