# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:57:57 2019

@author: BITTU
"""
import random

def partition(arr, l, h):
    index=random.randint(l,h)
    pivot , i= arr[index], (l-1)
    
    for j in range(h-1):
        if arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return (i+1)
    
def kthSmallest(arr, l, h, k):
    if k>0 and k<=h-l+1:
        p_index=partition(arr, l, h)
        
    if (p_index - l == k - 1):
        return arr[p_index]
  
        # If position is more, recur  
        # for left subarray 
    if (p_index - l > k - 1):
        return kthSmallest(arr, l, p_index - 1, k)
  
        #Else recur for right subarray 
    return kthSmallest(arr, p_index + 1, h,  
                            k - p_index + l - 1)


arr=[56,4,89,37,95,46,77,15]
n=len(arr)
print(n)
k=4
print("Unsorted array:")
for i in range(n):
    print(arr[i])

#quickSort(arr,0,n-1)
print("Kth smallest element is:",kthSmallest(arr, 0, n - 1, k))

#print("Sorted array:")
#for i in range(n):
#    print(arr[i])