"""The following implementation assumes that the activities 
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""

"""This algorithm implements greedy choice to select the activities"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 

import numpy as np

def printMaxActivities(s , f , p): 
    n = len(f)
   
    print ("The following activities are selected")

	# The first activity is always selected 
    i = 0
    profit=0
    print ("Job:",i)
    profit+=p[0]

	# Consider rest of the activities 
    for j in range(1,n): 

		# If this activity has start time greater than 
		# or equal to the finish time of previously 
		# selected activity, then select it 
            if s[j] >= f[i]: 
                print ("Job:",j) 
                profit+=p[j]
                i = j
    return profit                
# Driver program to test above function
if __name__ == '__main__':
 
    #s = [1 , 3 , 0 , 5 , 8 , 5] 
    #f = [2 , 4 , 6 , 7 , 9 , 9] 
    #p = [0 , 2 , 3 , 5 , 1 , 4]
    
    s=np.random.randint(1,100,500)
    s=sorted(s)
    f=np.random.randint(1,100,500)
    f=sorted(f)
    p=np.random.randint(1,100,500)
    profit=printMaxActivities(s , f , p) 
    print("Toatal Profit:",profit)
   
    # This code is contributed by Rahul Mukherjee 
