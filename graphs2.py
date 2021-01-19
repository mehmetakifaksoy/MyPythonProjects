import matplotlib.pyplot as plt
import numpy as np

goal_types = 'Penaltı','Kaleye atılan şut','Serbest Vuruş'
goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()