from EM import EM
from Auction_Simulator import Auction_Simulator
from numpy import average, std

def main():

	# Simulated Dataset 1
	f_mean = 4
	f_std = 3.5
	g_lam = 50 
	discount = .5
	num_auctions = 40
	num_datasets = 15
	num_trials = 20
	max_iterations = 1000
	error_fixg = []
	error = []
	auction = Auction_Simulator(f_mean, f_std, g_lam)

	data_1 = [[auction.simulate_initial_auction() for j in range(num_auctions)] for i in range(num_datasets)]
	# print auction.simulate_initial_auction()
	# print "g_ratio", average(auction.g_ratio), len(auction.g_ratio)
	for i in range(1):
		for j in range(num_auctions):
			auction_set, all_bids, num_bidders = data_1[i][j]

			em1 = EM(auction_set, discount, num_trials, max_iterations, all_bids)
			est_f_mean, est_f_std, est_g_lam = em1.learn()
			error_fixg.append( (est_f_mean - average(all_bids), est_f_std-std(all_bids), est_g_lam - num_bidders +2))

			em1 = EM(auction_set, discount, num_trials, max_iterations)
			est_f_mean, est_f_std, est_g_lam = em1.learn()
			error.append( (est_f_mean - average(all_bids), est_f_std-std(all_bids), est_g_lam - num_bidders +2))

			# print "RESULT AVG: ", est_f_mean, est_f_std, est_g_lam 

			# print "ACTUAL: ", average(all_bids), std(all_bids), num_bidders - 2

		error_sep= zip(*error_fixg)
		print "ERRORS FIX G: ", average(error_sep[0]), average(error_sep[1]), average(error_sep[2])

		error_sep = zip(*error)
		print "ERRORS: ", average(error_sep[0]), average(error_sep[1]), average(error_sep[2])

if __name__ == "__main__":
    main()
