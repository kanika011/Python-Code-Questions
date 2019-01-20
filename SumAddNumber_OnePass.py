#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

class Sums:
	def __init__(self):
		self.items=0
	def SumAddNumber(self, arr, n):
		"""
			:type: arr:int
			:type: n:int
			:rtype:bool
		"""
		for i in range(len(arr)):
			if n-arr[i] in arr:
				return True
		return False
		
arr=[10,15,3,7]
Obj=Sums()
print Obj.SumAddNumber(arr,17)
		