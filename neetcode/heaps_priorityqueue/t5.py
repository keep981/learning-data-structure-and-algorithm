#This submission i did in hurry during payoda interview. Not given much time to think, might have seen the answer quickly. The full understanding and how we reached the solution of the reason i might not have.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalAns2dList = []
        self.subsetHelper( nums, 0, [], finalAns2dList )
        return finalAns2dList

    def subsetHelper(self, nums, curIdxToWorkUpon, currentSubsetCarrier, finalAns2dList ):
        # For subset at a index, either we can take that or not 
        print(f"at subsetHelper:curIdxToWorkUpon={curIdxToWorkUpon}, currentSubsetCarrier={currentSubsetCarrier}")
        #Base condition
        if curIdxToWorkUpon == len(nums):
            finalAns2dList.append(currentSubsetCarrier)
            return
            
        #Will call the subproblem, also at that time solve for this idx by considering the index once and the next time not considering
        ##Not Considering current idx
        self.subsetHelper( nums, curIdxToWorkUpon + 1, currentSubsetCarrier, finalAns2dList )

        ##Considering current idx
        currentSubsetCarrier.append( nums[curIdxToWorkUpon] )
        self.subsetHelper( nums, curIdxToWorkUpon + 1, currentSubsetCarrier, finalAns2dList )
        currentSubsetCarrier.pop()  #We have to remove the current idx value before returning i.e backtracking
        

x = Solution()
nums = [ 17, 20, 23 ]
ans = x.subsets( nums )
print(ans)