A = np.array([[2,3,4],[6,7,6]])
B = np.array([[1,9,1],[2,3,9]])
C = np.array([[1, 4], [3, 4], [4,6]])
A+1
#array([ [3,4,5] , [7,8,7] ])
A * 2 
#array([ [4,6,8] , [12,14,12] ])
A ** 4 
#array([ [16,81,256] , [1296,2401,1296] ])
np.sin(A) 
#array([ [0.909,0.141,-0.756] , [-0.279,0.657,-0.279] ])
A + B 
#array([ [3,12,5] , [8,10,15] ])
A * B 
#array([ [2,27,4] , [12.21,54] ])
np.sum(A, axis = 0) #sum of the columns
#= A.sum(axis = 0) -> array([8,10,10])
np.sum(A, axis = 1) #sum of the rows
#= A.sum(axis = 1) -> array([9,19])

A @ C #matrix multiplication
A.dot(C) #matrix multiplication
#array([ [27, 44] , [51, 88] ])

a = np.array([1,2,3])
b = np.array([3,4,6])
a.dot(b) #29, scalar product