#Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.####

#To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

#To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        j=[]
        for i in A:
            j.append(i[::-1])
        m=[]
        for i in j:
            for k in range(len(i)):
                if i[k] == 1:
                    i[k] = 0
                else:
                    i[k]=1
        return j