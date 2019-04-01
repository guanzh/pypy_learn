import matplotlib.pyplot as plt
import numpy as np


def play_game_with_girl(malePro, femalePro, N, P):
	for j in range(P):
		maleG = []
		bG = 3
		lG = 1
		lo = -2

		for i in range(N):
			male = np.random.choice([1,0], 1, p=[malePro, 1-malePro])
			female = np.random.choice([1,0], 1, p=[femalePro, 1-femalePro])
			if male == 1 and female == 1:
				maleG.append(bG)
			elif male == 0 and female == 0:
				maleG.append(lG)
			else:
				maleG.append(lo)

		plt.plot(range(N), np.cumsum(maleG), color='red', alpha=0.15)
	plt.ylim(-120,120)
	plt.xlabel('Times')
	plt.ylabel('Gain')
	plt.show()


play_game_with_girl(malePro = 0.5,femalePro = 0.38, N = 50, P=100)


def play_game_with_girl2(malePro, femalePro, N, P):
	for j in range(P):
		maleG = []
		bG = 3
		lG = 1
		lo = -2
		male = np.random.choice([1,0], N, p=[malePro, 1-malePro])
		female = np.random.choice([1,0], N, p=[femalePro, 1-femalePro])
		for i in range(N):
			if male[i] == 1 and female[i] == 1:
				maleG.append(bG)
			elif male[i] == 0 and female[i] == 0:
				maleG.append(lG)
			else:
				maleG.append(lo)

		plt.plot(range(N), np.cumsum(maleG), color='red', alpha=0.15)
	plt.ylim(-120,120)
	plt.xlabel('Times')
	plt.ylabel('Gain')
	plt.show()


play_game_with_girl2(malePro = 0.5,femalePro = 0.38, N = 50, P=100)
