#Isomorphic strings
#Given two strings s and t, determine if they are isomorphic.

#Two strings are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

#Example 1:

#Input: s = "egg", t = "add"
#Output: true
#Example 2:

#Input: s = "foo", t = "bar"
#Output: false
#Example 3:

#Input: s = "paper", t = "title"
#Output: true

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        D={}
        i=0
        j=0
        while i<len(s):
            D[s[i]]=t[j]
            i=i+1
            j=j+1
        l=[]
        for i in D.values():
            l.append(i)
        l.sort()
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return False
        p=[]
        for k in range(0,len(s)):
            p.append(D.get(s[k]))
        if p == list(t):
            return True
        else:
            return False