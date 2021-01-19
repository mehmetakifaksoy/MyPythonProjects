import matplotlib.pyplot as plt
import numpy as np

yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [1,8,12,6,9]
oyuncu3 = [14,10,25,7,9]


#stack plot

plt.plot([],[],color="y", label = "oyuncu1")
plt.plot([],[],color="r", label = "oyuncu2")
plt.plot([],[],color="b", label = "oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3)

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.legend()
plt.ylabel("Gol sayisi")
plt.xlabel("yil")
plt.show()