import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

plt.figure(figsize=[6,3])
# plt.rcParams['figure.dpi'] = 200 #分辨率
# the histogram of the data
plt.hist(df['Normalized Score'],bins=50,color='lightgray',edgecolor='black',alpha=0.75)

plt.ylabel('Requests')

plt.axis([-3, 3, 0, 300])
plt.grid(True,linestyle='--',color='gray')

plt.show()
