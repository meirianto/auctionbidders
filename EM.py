from Auction_Simulator import Auction_Simulator
from numpy import average, std
class EM(object):

	def __init__(self, observed_bids, discount, num_trials, max_iterations):
		self.observed_bids = observed_bids
		self.discount = discount
		self.num_trials = num_trials
		self.max_iterations = max_iterations

	def learn(self):
		ok_err = 0.1
		f_mean_list = []
		f_std_list = []
		g_lam_list = []
		iterations = []
		hit_max = 0
		for i in range(self.num_trials):
			print "TRIAL : ", i
			f_mean = average(self.observed_bids)
			f_std = std(self.observed_bids)
			g_lam = len(self.observed_bids)-2
			iteration = 0			
			# print "START: ", iteration, f_mean, f_std, g_lam
			converged = False

			while not converged and iteration <= self.max_iterations:
				iteration += 1
				auction = Auction_Simulator(f_mean, f_std, g_lam)
				hidden_bids = auction.simulate_auction(self.observed_bids)
				highest_bid = [auction.simulate_highest(self.observed_bids)]

				all_bids = self.observed_bids + hidden_bids + highest_bid
				old_f_mean, old_f_std, old_g_lam = f_mean, f_std, g_lam
				f_mean, f_std = self.f_max(all_bids)

				#TODO: use estimated moving average to update g_lam
				# g_lam = self.discount*(len(all_bids)-2) + (1-self.discount)*g_lam
				# print "ITERATION: ", iteration, f_mean, f_std, g_lam
				g_lam = len(all_bids) - 2

				if (abs(old_f_mean-f_mean) <= ok_err and abs(old_f_std-f_std) <= ok_err and abs(old_g_lam-g_lam) <= ok_err):
					converged = True
			if iteration > self.max_iterations:
				hit_max += 1
			else:
				f_mean_list.append(f_mean)
				f_std_list.append(f_std)
				g_lam_list.append(g_lam)
				iterations.append(iteration)
				print "EM RESULT: ", f_mean, f_std, g_lam, iteration
	
		print " too many iterations %d times", hit_max
		return average(f_mean_list), average(f_std_list), average(g_lam_list)

	def f_max(self, bids):
		return average(bids), std(bids)