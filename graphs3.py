import matplotlib.pyplot as plt
import numpy as np


plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,80,100,65],label="BMW",width=0.5)
plt.bar([0.75,1.25,2.75,3.25,4.25],[80,20,25,50,65],label="Audi",width=0.5)

plt.legend()
plt.xlabel("gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")

plt.show()