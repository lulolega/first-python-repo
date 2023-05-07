import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(10).cumsum(), index = np.arange(0,100,10))

s.plot(color = 'red',style='2',alpha=0.3, label="домашняя работа", xlim[0;50])

plt.show()