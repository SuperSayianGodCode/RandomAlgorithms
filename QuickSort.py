# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:27:24 2019

@author: BITTU
"""
#import math

def partition(arr,l,h):
    
    i,j=(l-1),l
#    m=math.floor((l+h)/2)
    p=arr[h]
#    print("i ,j:",i,j)
#    print("pivot:",p)
    for j in range(l , h):
        if arr[j]<=p:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return ( i+1 )

def quickSort(arr,l,h):
    
    if l<h:
        p=partition(arr,l,h)
#        print("p:",p)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,n-1)
    
arr=[56,4,89,37,95,46,77,15]
n=len(arr)
print(n)

print("Unsorted array:")
for i in range(n):
    print(arr[i])

quickSort(arr,0,n-1)

print("Sorted array:")
for i in range(n):
    print(arr[i])
