import random

class deck:
	card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	
	def __init__(self):
		self.cards = []
		self.num_cards = 0		
		for card in deck.card_types:
			for x in range(0,4):
				self.num_cards += 1
				self.cards.append(card)
		random.shuffle(self.cards)
		
	def draw_card(self):
		if self.num_cards > 0:
			self.num_cards -= 1
			return self.cards.pop()
	
	def has_card():
		if self.num_cards > 0:
			return True
		else: return False
		
	def has_card(num):
		'''Returns True if deck has more cards than num'''
		if self.num_cards > num:
			return True
		else: return False
