from Auction_Simulator import Auction_Simulator
from numpy import average, std
class EM(object):

	def __init__(self, observed_bids):
		self.observed_bids = observed_bids
		self.f_mean = average(observed_bids)
		self.f_std = std(observed_bids)
		self.g_lam = None

	def learn():
		ok_err = 0.001
		converged = False
		while not converged:
			auction = Auction_Simulator(self.f_mean, self.f_std, self.g_lam)
			hidden_bids = auction.simulate_auction(self.observed_bids)
			highest_bid = auction.simulate_highest(self.observed_bids)

			all_bids = observed_bids + hidden_bids + highest_bid
			old_f_mean, old_f_std = self.f_mean, self.f_std 
			self.f_mean, self.f_std = self.f_max(all_bids)
			#TODO: something to update g_lam

			if ((old_f_mean-self.f_mean <= ok_err) and (old_f_std-self.f_std <= ok_err) and (old_g_lam-self.g_lam <= ok_err)):
			# TODO :: converged
				return self.f_mean, self.f_std, self.g_lam

	def f_max(self, bids):
		return average(bids), stdev(bids)