class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        treeNumbers = [1,1,2]
        for i in range(3,n+1):
            treeNumbers.append(0)
            for j in range(i):
                treeNumbers[i]+=treeNumbers[j]*treeNumbers[(i-1)-j]
        return treeNumbers[n]



sln=Solution()
assert 5 == sln.numTrees(3)
assert 14 == sln.numTrees(4)
assert 42 == sln.numTrees(5)