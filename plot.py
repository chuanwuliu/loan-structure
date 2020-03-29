import numpy as np
from matplotlib import pyplot as plt
from projection import project_wealth

p_tot = 490000
X = np.arange(0, 200000, 1000)
Y = [project_wealth(x, p_tot - x, period=3 * 12) for x in X]
plt.plot(X, Y)
plt.xlabel("Variable Loan Principal")
plt.ylabel("Not wealth")

plt.show()
