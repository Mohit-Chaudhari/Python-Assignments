import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def HeadBrainPredictor():

	# LOAD DATA
	data = pd.read_csv("MarvellousHeadBrain.csv")

	print("Size if data set",data.shape)

	x = data['Head Size(cm^3)'].values
	y = data['Brain Weight(grams)'].values

	# LEAST SQUARE METHOD
	mean_x = np.mean(x)
	mean_y = np.mean(y)

	n = len(x)

	numerator = 0
	denomenator = 0

	# EQUATION OF LINE IS Y = MX + C
	for i in range(n):
		numerator += (x[i]-mean_x)*(y[i]*mean_y)
		denomenator += (x[i]-mean_x)**2

	m = numerator / denomenator
	c = mean_y - (m * mean_x)

	print("Slope of regression line is",m)
	print("Y intercept of regression line is",c)

	max_x = np.max(x)+100
	min_x = np.max(x)-100

	# DISPLAYING PLOTTING OF ABOVE POINTS
	x = np.linspace(min_x,max_x,n)

	y = c + m * x

	plt.plot(x,y,color="#58b970",label="Regression line")
	plt.scatter(x,y,color="#ef5423",label="scatter plot")

	plt.xlabel('Head size in cm3')
	plt.ylabel('Brain weight in gram')

	plt.legend()
	plt.show()

	# FIND GOODNESS OF FIT i.e. R SQUARE
	ss_t = 0
	ss_r = 0

	for i in range(n):
		y_pred = c + x * x[i]
		ss_t += (y[i] - mean_y)**2
		ss_r += (y[i] - y_pred)**2

	r2 = 1 - (ss_r/ss_t)

	print(r2)


def main():
	print("Supervised machine learning")
	print("Linear regression on Head and Brain size data set")
	HeadBrainPredictor()

if __name__ == '__main__':
	main()