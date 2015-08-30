__author__ = 'Le Quang Hai'
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

test_data = np.random.normal(size=1000)

###################Boxplot################
plt.boxplot(test_data)
plt.show()

###################Histogram##############
plt.hist(test_data, histtype='bar')
plt.show()

###################QQ-plot###############
plt.figure()
qqPlot = stats.probplot(test_data,dist='norm', plot=plt)
plt.show()
