class Solution(object):
    def twoSum(self, nums, target):
        # nested for loop to read the list
        result = []
        # That's how my nested loop will works
        # and numbers represent index number
        """
        ---------------------------------------------
        |   left    |   0   |   1   |   2   |   3   |
        ---------------------------------------------
        |   right   |   1   |   2   |   3   |   x   |
        |   right   |   2   |   3   |       |   x   |
        |   right   |   3   |       |       |   x   |
        """
        for l in range(0,len(nums)):
            for r in range(1,len(nums)):
                left=nums[l]
                right=nums[r]
                t = nums[l] + nums[r]
                if(r>l and r!= l and t == target):
                    result.append(l)
                    result.append(r)
                    return result
s0 = Solution()
s1 = Solution()
s2 = Solution()
s3 = Solution()
print(s0.twoSum([2,7,11,15],9))
"""
2+7 CHECK
2+11
2+15
...
7+11
7+15
...
11+15
...
15+15
"""
print(s1.twoSum([3,2,4],6))
"""
3+2 CHECK
3+4
...
2+4
...
4+4
"""
print(s2.twoSum([3,3],6))
"""
3+3 CHECK
"""
print(s3.twoSum([2,5,5,11],10))
"""
index l=0, index r=1,2
2+5
2+5
2+11
...
index l=1,r=1,2
5+5 CHECK
5+11
...
11+11
"""