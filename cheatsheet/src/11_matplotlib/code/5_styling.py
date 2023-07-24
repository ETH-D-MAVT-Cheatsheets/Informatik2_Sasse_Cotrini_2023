fig, ax = plt.subplots()
ax.set_title("title") #add title
ax.set_xlabel("x label name") #set x-label
ax.set_ylabel("y label name") #set y-label
ax.legend() #add legend
#requires that you labeled your plots, i.e.: when calling
#ax.plot(X,Y, label="name of function").