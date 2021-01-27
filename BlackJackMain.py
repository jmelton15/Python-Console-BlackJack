import random
import blackjackMoney
import CardDeck
import colorama
from colorama import Fore, Back, Style

ready = ''
playing = True	




def hit_or_stand():
	go = ''
	try:
		go = input("Would you like to Hit or Stand?")
	except:
		print("Your response must be h,s,hit, or stand. Please try again!")
	else:
		if go.upper() == "H" or go.upper() == "HIT":
			return True
		else:
			return False


def replay():
	replay = ''
	if blackjackMoney.chipless(playerChips.total):
		print("You Lost All Your Chips. GAME OVER!")
		return False
	else:
		try:		
			replay = input("\nWould You like to play again?!")
		except:
			print("Your response must be y, n, yes, or no. Please try again")
		else:
			if replay.upper() == "Y" or replay.upper() == "YES":
				print('\n'*100)
				return True
			else:
				print("Thanks For Playing! .. Game Has Ended")
				return False









print("Welcome to BlackJack!")

playerChips = blackjackMoney.Chips()

while True:

	try:
		ready = input("\nAre you ready to play?!")
	except:
		print("Your response must be y, n, yes, or no. Please try again")
		continue
	else:
		if ready.upper() == 'Y' or ready.upper() == 'YES':
			gameInSession = True
		if ready.upper() == 'N' or ready.upper() == 'NO':
			print("Game Ended by User")
			gameInSession = False
		else:
			gameInSession = True


	while gameInSession:
		#global playerChips
		# Here we create chips object for player and take the bet for the hand
		aceCount = 0
		blackjackMoney.bet(playerChips)


		# Here we create the hand objects for player and computer
		# We start the hit stand process
		liveGame = CardDeck.Hand()
		liveGame.deal()
		CardDeck.show_some_cards(liveGame.playerHand,liveGame.computerHand)
		liveGame.add_player_hand(liveGame.playerHand)
		liveGame.add_computer_hand(liveGame.computerHand)
		print(Fore.BLACK + Back.WHITE) 
		print("Your Current Hand Value is: {}  ".format(liveGame.initialPlayerHandValue))
		print(Style.RESET_ALL)
		if liveGame.pAces > 0 and aceCount == 0:
			liveGame.adjust_for_player_ace(liveGame.playerRunningTotal,liveGame.pAces)
			aceCount += 1
		if liveGame.initialPlayerHandValue == 21:
			blackjackMoney.player_blackjack(liveGame.playerHand,liveGame.computerHand,playerChips)
			print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
			gameInSession = False
			
		elif liveGame.initialPlayerHandValue != 21 and liveGame.initialCompHandValue == 21:
			blackjackMoney.dealer_blackjack(liveGame.playerHand,liveGame.computerHand,playerChips)
			print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
			gameInSession = False
		else:
			while hit_or_stand():
				liveGame.hit(liveGame.playerHand)
				CardDeck.show_some_cards(liveGame.playerHand,liveGame.computerHand)
				liveGame.add_player_hand(liveGame.playerHand)
				liveGame.adjust_for_player_ace(liveGame.playerRunningTotal,liveGame.pAces)
				if liveGame.playerRunningTotal > 21:
					print(Fore.BLACK + Back.WHITE)
					print("Your Hand Value {} is over 21. ".format(liveGame.playerRunningTotal))
					print(Style.RESET_ALL)
					blackjackMoney.player_busts(liveGame.playerHand,liveGame.computerHand,playerChips)
					print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
					gameInSession = False
					break
				else:
					#print("Your Hand Value is: {}".format(liveGame.playerRunningTotal))
					continue
			if gameInSession == False:
				break	
			CardDeck.show_all_cards(liveGame.playerHand,liveGame.computerHand)
			print(Fore.BLACK + Back.WHITE)
			print("\nDealer's Current Hand Value is: {}  ".format(liveGame.initialCompHandValue))
			print(Style.RESET_ALL)
			while liveGame.compRunningTotal < 17:
				liveGame.hit(liveGame.computerHand)
				CardDeck.show_all_cards(liveGame.playerHand,liveGame.computerHand)
				liveGame.add_computer_hand(liveGame.computerHand)
				print(Fore.BLACK + Back.WHITE)
				print("\nDealer's New Hand Value is: {}  ".format(liveGame.compRunningTotal))
				print(Style.RESET_ALL)

			if liveGame.compRunningTotal > 21:
				print(Fore.BLACK + Back.WHITE)
				blackjackMoney.dealer_busts(liveGame.playerHand,liveGame.computerHand,playerChips)
				print(Style.RESET_ALL)
				print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
				gameInSession = False
				break

			if liveGame.compRunningTotal > liveGame.playerRunningTotal and liveGame.initialCompHandValue != 21:
				print(Fore.BLACK + Back.WHITE)
				print("Dealer's Hand Value is: {} and Your Hand Value is: {}  ".format(liveGame.compRunningTotal,liveGame.playerRunningTotal))
				print(Style.RESET_ALL)
				blackjackMoney.dealer_wins(liveGame.playerHand,liveGame.computerHand,playerChips)
				print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
				gameInSession = False
				break
			
			if liveGame.playerRunningTotal > liveGame.compRunningTotal and liveGame.initialPlayerHandValue != 21:
				print(Fore.BLACK + Back.WHITE)
				print("Dealer's Hand Value is: {} and Your Hand Value is: {}  ".format(liveGame.compRunningTotal,liveGame.playerRunningTotal))
				print(Style.RESET_ALL)
				blackjackMoney.player_wins(liveGame.playerHand,liveGame.computerHand,playerChips)
				print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total))
				gameInSession = False
				break
			
			if liveGame.compRunningTotal == liveGame.playerRunningTotal:
				print(Fore.BLACK + Back.WHITE)
				print("Dealer's Hand Value is: {} and Your Hand Value is: {}  ".format(liveGame.compRunningTotal,liveGame.playerRunningTotal))
				print(Style.RESET_ALL)
				blackjackMoney.push(liveGame.playerHand,liveGame.computerHand)
				print("Your chip count is:",str(playerChips.total))
				gameInSession = False
				break
			else:
				print(Style.BRIGHT + "Your chip count is now:",str(playerChips.total)) 
				gameInSession = False
				break

	if not replay():
		print("Thanks For Playing! ... You Have Left The Table")
		break
	
			


			




	
				


