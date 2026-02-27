import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


#Labels:
# x = np.array([10,17,32,54,65])
# y = np.array([14,25,37,59,75])
# plt.title(["Average Sports Watch Data"])
# plt.xlabel("Average Pulse")
# plt.ylabel('Calorie Pulse')
# plt.plot(x,y)
# plt.show()


#
# font1 = {'family':'serif', 'color': 'blue', 'size': 20}
# font2 = {'family':'serif', 'color': 'red', 'size': 15}
# x = np.array([10,17,32,54,65])
# y = np.array([14,25,37,59,75])
# plt.title("Average Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font1)
# plt.ylabel('Calorie Pulse', fontdict = font2)
# plt.plot(x,y)
# plt.show()

# Grid




#Subplot
#plot-1
x = np.array([10,20,30,40])
y = np.array([2,3,4,5])
plt.subplot(2,1,1)
plt.plot(x,y)


#Plot-2
x = np.array([20,40,60,80])
y = np.array([13,24,33,65])
plt.subplot(2,1,2)
plt.plot(x,y)


plt.show()