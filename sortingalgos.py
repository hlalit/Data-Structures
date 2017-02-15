import numpy as np

class sortingalgos:
    def __init__(self):
        self.root = None
        
    def bubble_sort(self):
        
        x = np.array([3,7,4,9,5,2,6,1])
        n = x.shape[0]
        for i in range(0,n):
            for j in range(0,n-1-i):
                if(x[j] > x[j+1]):
                    t = x[j]
                    x[j] = x[j+1]
                    x[j+1] = t
            
        return x
    
    def selection_sort(self):
        
        x = np.array([3,7,4,9,5,2,6,1])
        n = x.shape[0]
        for i in range(0,n):
            initMin = i
            for j in range(i+1,n):
                if(x[j] < x[initMin]):
                    initMin = j
                    
            t = x[initMin]
            x[initMin] = x[i]
            x[i] = t
            
        return x
    
    def insertion_sort(self):
        
        x = np.array([3,7,4,9,5,2,6,1])
        n = x.shape[0]
        for i in range(0,n):
            for j in range(i,0,-1):
                if(x[j] < x[j-1]):
                    t = x[j]
                    x[j] = x[j-1]
                    x[j-1] = t
        return x

obj = sortingalgos()
x1 = obj.bubble_sort()
print(x1)
print()
x2 = obj.selection_sort()
print(x2)
print()
x3 = obj.insertion_sort()
print(x3)