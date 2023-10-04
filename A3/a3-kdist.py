# Plot k-distances
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def k_distances(X, n=None):
    if type(X) is pd.DataFrame:
        X = X.values
    k=0
    if n == None:
        k=X.shape[1]+2
    else:
        k=n+1
    dist_func = lambda x, y: math.sqrt(np.sum(np.power(x-y, np.repeat(2,x.size))))
    Distances = pd.DataFrame({
        "i": [i//10 for i in range(0, len(X)*len(X))],
        "j": [i%10 for i in range(0, len(X)*len(X))],
        "d": [dist_func(x,y) for x in X for y in X]
    })
    return np.sort([g[1].iloc[k].d for g in iter(Distances.groupby(by="i"))])

# TODO: add your parameters here.
# data -- your normalized dataset (dataframe matrix)
# k    -- k-th neighbour (for distance metric). By default, k=count(features)+1
d = k_distances(
    # data,
    # k 
)
plt.plot(d)
plt.ylabel("k-distances")
plt.grid(True)
plt.show()