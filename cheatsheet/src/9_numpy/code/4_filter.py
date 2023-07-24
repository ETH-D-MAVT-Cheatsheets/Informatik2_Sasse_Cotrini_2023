a = np.arange(7) #array([0,1,2,3,4,5,6])
f = a % 2 == 0 #f = [True, False, True, False, True, False, True]
a[f] #array([0,2,4,6])