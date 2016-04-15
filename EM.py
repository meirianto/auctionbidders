from Auction_Simulator import Auction_Simulator
from numpy import average, std
class EM(object):

	def __init__(self, observed_bids, discount):
		self.observed_bids = observed_bids
		self.f_mean = average(observed_bids)
		self.f_std = std(observed_bids)
		self.g_lam = None 
		self.discount = discount

	def learn(self):
		ok_err = 0.1
		converged = False
		self.g_lam = len(self.observed_bids)
		iterations = 0
		print "START: ", iterations, self.f_mean, self.f_std, self.g_lam

		while not converged:
			iterations += 1
			auction = Auction_Simulator(self.f_mean, self.f_std, self.g_lam)
			hidden_bids = auction.simulate_auction(self.observed_bids)
			highest_bid = [auction.simulate_highest(self.observed_bids)]

			all_bids = self.observed_bids + hidden_bids + highest_bid
			old_f_mean, old_f_std, old_g_lam = self.f_mean, self.f_std, self.g_lam
			self.f_mean, self.f_std = self.f_max(all_bids)

			#TODO: use estimated moving average to update g_lam
			self.g_lam = self.discount*len(all_bids) + (1-self.discount)*self.g_lam
			print "ITERATION: ", iterations, self.f_mean, self.f_std, self.g_lam

			if (abs(old_f_mean-self.f_mean) <= ok_err and abs(old_f_std-self.f_std) <= ok_err and abs(old_g_lam-self.g_lam) <= 20*ok_err):
				converged = True
				# print self.f_mean, self.f_std, self.g_lam, iterations
		
		return self.f_mean, self.f_std, self.g_lam, iterations

	def f_max(self, bids):
		return average(bids), std(bids)