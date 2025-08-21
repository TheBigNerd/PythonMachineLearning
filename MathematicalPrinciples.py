import numpy as np
from scipy import stats

# Mean, Median and Mode
# Mean - The average value
# Median - The midpoint value
# Mode - The most common value

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed)
print(mean)
median = np.median(speed)
print(median)
mode = stats.mode(speed)
print(mode)

# Standard Deviation = How spread our the values are

sD = np.std(speed)
print(sD)

# Variance = Another number indicating how spread out values are (Variance is the Standard Deviation squared)

var = np.var(speed)
print(var)

# Percentiles = A number that describes the value that a given percent of the values are lower than

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 75)
# Gives out the number that 75% of people are or are younger than
print(x)

