import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,color="red",linewidth="6")
plt.axis([0,6,0,20])

plt.title("Grafik")
plt.xlabel("x label")
plt.ylabel("y label")

plt.show()
