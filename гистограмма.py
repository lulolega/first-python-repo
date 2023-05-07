import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)
data = pd.Series(np.random.rand(5), index = list('jrgyu'))
data.plot.bar(ax = axes[0], color = 'k')

plt.show()