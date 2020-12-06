import math
import random

class Deck():
	suits = ['clubs', 'hearts', 'spades', 'diamonds']
	values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

	def __init__(self):
		self.deck = []
		for number in range(1, 55):
			self.deck.append(number)	
	
	def draw_new_character(self):
		pass
	
	def draw(self):
		return self.deck.pop(random.randint(0, len(self.deck) -1))

	def get_cards_normal(self, number):
		cards = []
		for _ in range(1, number+1):
			cards.append(self.convert_to_card(self.draw()))
		return cards	
	
	def convert_to_card(self, number):
		if number == 53:
			return "Black Joker"
		if number == 54:
			return "Red Joker"

		suit = self.suits[math.floor((number-1)/13)]
		value = self.values[(number % 13) -1]
		return (f"{value} of {suit}")

#print(d.convert_to_card(54))
for _ in range(1, 100):
	d = Deck()
	print(d.get_cards_normal(5))
