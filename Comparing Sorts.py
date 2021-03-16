'''Esther Edwards 
Algorithm Analysis
Program 2
This program compares sorts of two types by their runtime calculated 
by the system's clock. There will be two O(n^2) sorting algorithms
compared and two O(n logn) algorithms compared. Each runtime will be 
calculated and saved in a csv file which will then be used to plot 
graphs.
'''
import random
import time
import csv
#from time import perf_counter


def main():
    size = 10
    nums = []
    allLists = []
    fullList = []

    for i in range(9):
        #fill the array
        arr = fillArray(nums, size)
        fullList = createLists(arr)
    
    print(fullList[0])
    createFile(fullList[0], fullList[1])
    

'''
Fill Array
function to create array filled with random numbers
'''
def fillArray(nums, size):
  random.seed(3) 
  nums = [] 
  for x in range(size):
    nums.append(random.randint(1, 1000))
  
  return nums


'''
Create Lists
Function to created the list of times from each of the sorts
'''
def createLists(arr):
    gnomeTimes = []
    cocktailSortTimes = []
    combinedLists = []
    #start timer
    startTime = time.time()
    #sort the array
    gnomeSort(arr)
    endTime = time.time() #end timer 
    runTime = (endTime - startTime)#* (10**6)
    #add the time to a list
    gnomeTimes.append(runTime)
    combinedLists.append(gnomeTimes)

    startTime = time.time()
    cocktailSort(arr)
    endTime = time.time() #end timer 
    runTime = (endTime - startTime)#* (10**6)
    cocktailSortTimes.append(runTime)
    combinedLists.append(cocktailSortTimes)

    return combinedLists




'''
Gnome Sort
# A function to sort the given list using Gnome sort 
# taken from geeksforgeeks.org
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
'''
def gnomeSort( arr):
  n = len(arr) 
  index = 0
  while index < n: 
      if index == 0: 
          index = index + 1
      if arr[index] >= arr[index - 1]: 
          index = index + 1
      else: 
          arr[index], arr[index-1] = arr[index-1], arr[index] 
          index = index - 1
  return arr 



'''
Cocktail Sort
Python program for implementation of Cocktail Sort 
Taken from GeeksforGeeks
'''
def cocktailSort(a): 
	n = len(a) 
	swapped = True
	start = 0
	end = n-1
	while (swapped==True): 

		# reset the swapped flag on entering the loop, 
		# because it might be true from a previous 
		# iteration. 
		swapped = False

		# loop from left to right same as the bubble 
		# sort 
		for i in range (start, end): 
			if (a[i] > a[i+1]) : 
				a[i], a[i+1]= a[i+1], a[i] 
				swapped=True

		# if nothing moved, then array is sorted. 
		if (swapped==False): 
			break

		# otherwise, reset the swapped flag so that it 
		# can be used in the next stage 
		swapped = False

		# move the end point back by one, because 
		# item at the end is in its rightful spot 
		end = end-1

		# from right to left, doing the same 
		# comparison as in the previous stage 
		for i in range(end-1, start-1,-1): 
			if (a[i] > a[i+1]): 
				a[i], a[i+1] = a[i+1], a[i] 
				swapped = True

		# increase the starting point, because 
		# the last stage would have moved the next 
		# smallest number to its rightful spot. 
		start = start+1

'''
Create File function
Description: This function takes the lists of times and puts them in a CSV file
'''
def createFile(listA, listB):
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    
    print(listA)
    x = np.arange(0, 10000, 1000)
    f, (graph1, graph2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[1, 1]}, sharex=True, figsize=(10,10))
    #f, (graph1, graph2) = plt.subplots(2,1, {'height_ratios':[1, 1]}, sharex=True, sharey=False, squeeze=True, subplot_kw=None, figsize=(10,10)) 
    graph1.grid()
    graph2.grid()

    #setting up each line to be plotted and labels
    graph1.plot(x,listA,linestyle='-',marker='o',label='Gnome Sort',color='blue' )
    graph1.plot(x,listB,linestyle='-',marker='o',label='Cocktail Shaker Sort',color='red' )
    graph1.legend()
    graph1.titleset('O(n^2) graphs')
    graph1.set_xticks([])
    
    plt.savefig(write_file)
    # call with no parameters
    plt.legend()
    plt.show()

    



if __name__ == "__main__":
    main()