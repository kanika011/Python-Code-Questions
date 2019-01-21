#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

#You may return any answer array that satisfies this condition.

 

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        O=[]
        E=[]
        for i in A:
            if i%2 == 0:
                E.append(i)
            else:
                O.append(i)
        for i in range(len(O)):
            E.append(O[i])
        return E
            
        