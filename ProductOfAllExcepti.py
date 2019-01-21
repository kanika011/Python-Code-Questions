#Given an array of integers, return a new array such that each element at 
#index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def Prod(arr):
	M=1
	ans=[]
	for i in range(len(arr)):
		M=M*arr[i]
	for i in range(len(arr)):
		ans.append(M/arr[i])
	return ans
arr=[1,2,3,4,5]
print(Prod(arr))
arr1=[3,2,1]
print(Prod(arr1))