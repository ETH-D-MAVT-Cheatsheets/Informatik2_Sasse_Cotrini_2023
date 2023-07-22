import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,2*np.pi,30)
Y = np.sin(X)

fig, ax = plt.subplots()
ax.plot(X,Y) #line plot
ax.scatter(X,Y) #scatter plot