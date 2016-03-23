from EM import EM
from Auction_Simulator import Auction_Simulator

def main():

	# Simulated Dataset 1
	f_mean = 4
	f_std = 3.5
	g_lam = 40 
	num_auctions = 40
	num_datasets = 15
	auction = Auction_Simulator(f_mean, f_std, g_lam)

	#data_1 = [[auction.simulate_initial_auction() for k in range(num_auctions)] for i in range(num_datasets)]
	# print data_1[0][0], len(data_1[0][0])
	print auction.simulate_initial_auction()

	# em1 = EM(auction_set)
	# est_f_mean, est_f_std, est_g_lam = em1.learn()

if __name__ == "__main__":
    main()
