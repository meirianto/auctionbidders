from numpy.random import normal, poisson

class Agent(object):
	def __init__(self, f_mean, f_std):
		self.f_mean = f_mean
		self.f_std = f_std
	def get_bid(self):
		bid = -1
		while bid <= 0:
		  bid = normal(self.f_mean, self.f_std)
		return bid

class Auction_Simulator(object):

	"""simulate dataset of observed bids"""

	def __init__(self, f_mean, f_std, g_lam):
		""" f(x) is  N(f_mean, f_std)"""
		""" g(x) is Poisson(g_theta)"""

		self.f_mean = f_mean
		self.f_std = f_std
		self.g_lam = g_lam
		self.g_ratio = []

	def simulate_initial_auction(self):
		"""generate dataset of observed bids and number of bidders for initial auction"""
		num_bidders = poisson(self.g_lam) + 2 # number of bidders is at least 2
		agent = Agent(self.f_mean, self.f_std)
		observed_bids, hidden_bids = [], []
		price =  0
		highest = agent.get_bid() #generate first bid
		# print highest, "HIGHEST"
		for i in range(num_bidders-1):
			cur_bid = agent.get_bid()
			if cur_bid < price:
				"""dropped aka hidden"""
				hidden_bids.append(cur_bid)
				# print cur_bid, "HIDDEN"
			elif cur_bid > highest:
				"""new highest proxy bid, old highest bid become price and is seen"""
				observed_bids.append(highest)
				price = highest
				highest = cur_bid 
				# print cur_bid, "HIGHEST"

			else:
				"""cur_bid becomes new price"""
				price = cur_bid
				observed_bids.append(cur_bid)
				# print cur_bid, "OBSERVED"

		# print
		# print "TOTAL", num_bidders, "NUM OBSERVED", len(observed_bids), " NUM HIDDEN", len(hidden_bids), " HIGHEST", highest, " PRICE", price
		# print "==============================="
		all_bids = observed_bids + hidden_bids + [highest]

		self.g_ratio.append(num_bidders/len(observed_bids))
		return observed_bids, all_bids, num_bidders

	def simulate_auction(self, observed_bids):
		"""the E step of EM, to simulate set of dropped bids"""
		agent = Agent(self.f_mean, self.f_std)

		while True:
			hidden_bids = []
			
			num_bidders = 0
			while num_bidders<len(observed_bids)+1:
				num_bidders = poisson(self.g_lam, 1) + 2 # number of bidders is at least 2
				num_dropped = num_bidders - len(observed_bids) - 1

			idx_price = 0
			while True: #action runs
				cur_bid = agent.get_bid()
				price = observed_bids[idx_price]
				if cur_bid < price:
					"""dropped aka hidden"""
					hidden_bids.append(cur_bid)
				else:
					"""next lowest observed bid becomes price"""
					idx_price += 1
				if idx_price == len(observed_bids):
				 	if len(hidden_bids) == num_dropped:
						return hidden_bids
					break

	def simulate_highest(self, observed_bids):
		price = max(observed_bids)
		bid = None
		while bid <= price:
			agent = Agent(self.f_mean, self.f_std)
			bid = agent.get_bid()
		return bid
