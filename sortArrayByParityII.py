#Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

#Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

#You may return any answer array that satisfies this condition.

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        O=[]
        E=[]
        for i in A:
            if i%2==0:
                E.append(i)
            else:
                O.append(i)
        M=[]
        i=0
        j=0
        while i<len(A):
            M.append(E[j])
            M.append(O[j])
            i+=2
            j+=1
        return M
            