import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("ATX_market_caps.csv", sep=";")

df = df.set_index("Code")
df = df.replace("NA", np.nan)
df = df.astype(float)

df.index = pd.to_datetime(df.index, dayfirst=True)
df = df.sort_index()

# numpy arrays
caps = df.values

# ranked indices
argsort = np.argsort(caps, axis=1)[:, ::-1]

# sorted caps
sorted_caps = np.take_along_axis(caps, argsort, axis=1)

df_argsort = pd.DataFrame(argsort, index=df.index, columns=df.columns)
df_sorted = pd.DataFrame(sorted_caps, index=df.index, columns=df.columns)

with open("ATX.pickle", "wb") as f:
    pickle.dump((df_argsort, df_sorted), f)
