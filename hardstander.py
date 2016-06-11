class HardStander:
	NATURAL = 1
	STAND = 2
	BUST = 3
	
	def __init__(self, stand_at):
		self.stand = stand_at
		self.num_hits = 0
		self.num_aces = 0
		self.num_hard_aces = 0
		self.hand_sum = 0

	def state(self):
		if (num_hits == 0) and (hand_sum == 21):
			return NATURAL
		elif self.hand_sum > 21:
			return BUST
		elif self.hand_sum > self.stand:
			return STAND

	def get_card_value(card):
		return {
        	'2': 2,
        	'3': 3,
        	'4': 4,
        	'5': 5,
        	'6': 6,
        	'7': 7,
        	'8': 8,
        	'9': 9,
        	'10': 10,
        	'J': 10,
        	'Q': 10,
        	'K': 10
    	}.get(card)	

	def hit(self, card):
		self.num_hits += 1
		if card == 'A':
			self.num_aces += 1
			self.hand_sum += 11
		
		self.hand_sum += get_card_value(card)
		
		if (self.hand_sum > 21) and (self.num_hard_aces < self.num_aces):
			self.num_hard_aces += 1
			self.hand_sum -= 10
