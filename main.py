from EM import EM
from Auction_Simulator import Auction_Simulator
from numpy import average, std

def main():

	# Simulated Dataset 1
	f_mean = 4
	f_std = 3.5
	g_lam = 40 
	discount = .5
	num_auctions = 40
	num_datasets = 15
	auction = Auction_Simulator(f_mean, f_std, g_lam)

	data_1 = [[auction.simulate_initial_auction() for k in range(num_auctions)] for i in range(num_datasets)]
	# print auction.simulate_initial_auction()
	# print "g_ratio", average(auction.g_ratio), len(auction.g_ratio)

	auction_set, all_bids, num_bidders = data_1[0][0]

	em1 = EM(auction_set, discount)
	est_f_mean, est_f_std, est_g_lam, iterations = em1.learn()

	print "RESULT: ", iterations, est_f_mean, est_f_std, est_g_lam

	print "ACTUAL: ", average(all_bids), std(all_bids), num_bidders

if __name__ == "__main__":
    main()
