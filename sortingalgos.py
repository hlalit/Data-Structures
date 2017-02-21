import numpy as np
import math as mt

class sortingalgos:
    def __init__(self):
        self.root = None
        
    def bubble_sort(self,x,n):
        
        x1 = x.copy()        
        for i in range(0,n):
            for j in range(0,n-1-i):
                if(x1[j] > x1[j+1]):
                    t = x1[j]
                    x1[j] = x1[j+1]
                    x1[j+1] = t
            
        return x1
    
    def selection_sort(self,x,n):
        
        x1 = x.copy() 
        for i in range(0,n):
            initMin = i
            for j in range(i+1,n):
                if(x1[j] < x1[initMin]):
                    initMin = j
                    
            t = x1[initMin]
            x1[initMin] = x1[i]
            x1[i] = t
            
        return x1
    
    def insertion_sort(self,x,n):
        
        for i in range(0,n):
            for j in range(i,0,-1):
                if(x1[j] < x1[j-1]):
                    t = x1[j]
                    x1[j] = x1[j-1]
                    x1[j-1] = t
        return x1
    
    def partition(self,x1,start,end):
        pivot = x1[end]
        pindex = start 
        
        for i in range(start,end):
            if(x1[i] <= pivot):
                t = x1[i]
                x1[i] = x1[pindex]
                x1[pindex] = t
                pindex = pindex + 1
        
        t = x1[pindex]
        x1[pindex] = x1[end]
        x1[end] = t
        return pindex
    
    def quick_sort(self,x1,start,end):
        
        if(start < end):
            pindex = self.partition(x1,start,end)
            self.quick_sort(x1,start,pindex - 1)
            self.quick_sort(x1,pindex + 1,end)
        return x1
    
    def merge(self,La,Lb):
    
        l1 = La.shape[0]
        l2 = Lb.shape[0]
        Lc = []
        i = 0
        j = 0
        while (i < l1 and j < l2):
            if(Lb[j] < La[i]):
                Lc.append(Lb[j])
                j = j + 1 
                continue
            
            if(Lb[j] > La[i]):
                Lc.append(La[i])
                i = i + 1 
                continue
            
            if(Lb[j] == La[i]):
                Lc.append(La[i])
                i = i + 1 
                j = j + 1 
                continue
            
        if(i == l1):
            while j < l2:
                Lc.append(Lb[j])
                j = j + 1 
        if (j == l2):
            while i < l1:
                Lc.append(La[i])
                i = i + 1 
        
        Lc = np.array(Lc)
        return Lc
    
    def mergesort(self,x1,start,end):
        
        if(start < end):
            print(x1)
            mid = mt.ceil((start + end)/2)
            left = x1[start:mid]
            right = x1[mid:end]
            
            self.mergesort(left,start,mid-1)
            self.mergesort(right,mid,end)
            x1 = self.merge(left,right)
        return x1
                
x = np.array([3,7,4,9,5,2,1,6])
n = x.shape[0]
start = 0
end = n-1

obj = sortingalgos()
x1 = obj.bubble_sort(x,n)
print(x1)
x2 = obj.selection_sort(x,n)
print(x2)
x3 = obj.insertion_sort(x,n)
print(x3)
x1 = x.copy()
x4 = obj.quick_sort(x1,start,end)
print(x4)
x1 = x.copy()
x5 = obj.mergesort(x1,start,end)
print(x5)
