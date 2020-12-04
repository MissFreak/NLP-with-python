import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=[2,0.5])
df["Label"].reset_index().groupby("Label").count().sort_values(by= 
       "index").plot(kind="barh", legend=False, 
        ax=ax).grid(axis='x')
plt.show()
