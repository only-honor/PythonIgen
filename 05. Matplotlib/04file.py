#Histograms:
import numpy as np
import matplotlib.pyplot as plt




#Histograms
#x = np.random.normal(170,10,250)
#print(x)
# plt.hist(x)
# plt.show()




#Piechart
# x = np.array(['Apples', 'Bananas', 'Cherry', 'Kiwi'])
# y = np.array([35,25,15,10])
# #plt.pie(x,y) #Will show error due to x, as it contains string value
# plt.pie(y) #correct way
# plt.show()




z = np.array(['Apples', 'Bananas', 'Cherry', 'Kiwi'])
y = np.array([35,25,15,10])

plt.pie(y, labels = z) 
plt.show()




