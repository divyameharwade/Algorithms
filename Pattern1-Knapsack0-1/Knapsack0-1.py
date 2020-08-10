""" Problem statement -  Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it. """

# weights = [1, 2, 3, 5]
# profits = [1, 6, 10, 16]
# cap = 7
# Max profit = 22
# Chosen weights = [5, 2]
# dp = [[0, 1, 1, 1, 1, 1, 1, 1], 
#		[0, 1, 6, 7, 7, 7, 7, 7], 
#		[0, 1, 6, 10, 11, 16, 17, 17], 
#		[0, 1, 6, 10, 11, 16, 17, 22]]

# SIMPLE RECURSION:
# Time Complexity - O(2^n)
# Space Complexity - O(n)
def knapsack(profits, weights, cap, index):
    # base case
    if cap<=0 or index<0 or index>=len(profits):
        return 0
    profit1 = 0
    profit2 = 0
    if weights[index] <= cap:
        profit1 = profits[index] + knapsack(profits, weights, cap-weights[index], index+1)
    else:
        profit2 = knapsack(profits, weights, cap, index+1)
    return max(profit1, profit2)

# TOP-DOWN APPROACH
# Varying params are : cap and index so create dp[index][cap+1] and compute the profits for every cell
# Time Complexity - O(n*cap)
# Space Complexity - O(n*cap + n) [dp and recursion stack

def knapsack(profits, weights, cap, index):
	# Initialize the dp
	# dp = [[None for j in range(cap+1)] for i in range(len(weights))]

	# base case
	if cap<=0 or index<0 or index>=len(profits):
		return 0
	print(index, cap)
	if dp[index][cap]: 
		return dp[index][cap]

	profit1 = 0
	profit2 = 0
	if weights[index] <= cap:
		profit1 = profits[index] + knapsack(profits, weights, cap-weights[index], index+1)
	else:
		profit2 = knapsack(profits, weights, cap, index+1)
	dp[index][cap] =  max(profit1, profit2)
	return dp[index][cap]

# BOTTOM UP APPROACH 
# Modifications include - 
#	1) initializing the first column with 0
#	2) initializing first row with weight of first element (single element case)
#	3) For loops starting from 1
#	4) modify value only if weight <= cap
#Time Complexity - O(n*cap)
#Space Complexity - O(n*cap)

def knapsack(profits, weights, cap):
	# Initialize the dp
	dp = [[None for j in range(cap+1)] for i in range(len(weights))]
	# base case
	for i in range(len(weights)):
		dp[i][0] = 0
	for j in range(cap+1):
		if weights[0] <= j:
			dp[0][j] = profits[0]
	for i in range(1, len(weights)):
		profit1 = 0
		profit2 = 0
		for j in range(1,cap+1):
			if weights[i] <= j:
				profit1 =  profits[i]+dp[i-1][j-weights[i]]

			profit2 = dp[i-1][j]
			dp[i][j] = max(profit1, profit2)
	print(dp)
	return  dp[len(weights)-1][cap]

# BOTTOM UP APPROACH WITH SPACE OPTIMIZATION
# Modifications - using a 1D array
# - using the inner loop in reverse order to avoid values from being overriden before computation
# We can reduce the space by using a single array. 
# Time Complexity - O(n*cap)
# Space Complexity - O(n)
def knapsack(profits, weights, cap):
	# Initialize the dp
	dp = [0 for j in range(cap+1)]

	# base case

	dp[0] = 0

	for j in range(cap+1):
		if weights[0] <= j:
			dp[j] = profits[0]

	for i in range(1, len(weights)):
		profit1 = 0
		profit2 = 0 
		# looping from right to left 
		for j in range(cap,0,-1):
			if weights[i] <= j:
				profit1 =  profits[i]+dp[j-weights[i]]
			
			profit2 = dp[j]
			dp[j] = max(profit1, profit2)
	print(dp)
	return  dp[cap]

# FIND THE CHOSEN WEIGHTS (works only with the 2D dp array) 
result = []
i =  len(weights)-1
j = cap
while(i>0 and j>0):
	if dp[i][j]!=dp[i-1][j]:
		result.append(weights[i])
		j =  j-weights[i]
	i = i -1


