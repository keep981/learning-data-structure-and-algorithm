class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # This test case of input where there is no interval earlier in the intervals list, but another newInterval is added. I missed this
        if len(intervals) == 0:
            return [newInterval[:]]
            
        ans = []
        itrIdx = 0
        #Finding till which index the starting of newInterval is less than the start of any interval
        while itrIdx < len(intervals) and newInterval[0] >= intervals[itrIdx][0] :
            itrIdx += 1

        # Append everything in the range [0:itrIdx-1], remember this 
        #Two cases we have to handle now,
        #   i. that is newInterval start is smaller than first element it self, so it will go to the front
        #   ii. It lies inbetween or after everything ends
        # Now we will decide what will be the starting interval 
        if itrIdx == 0:
            if newInterval[1] < intervals[0][0]: #New interval is fully before the already existing interval list
                ans.append( newInterval[:] )
                ans.extend( [ x[:] for x in intervals ] )
                return ans
            elif newInterval[1] <= intervals[0][1]:  #New interval ending is within the first interval
                ans.append( [newInterval[0], intervals[0][1]] )
                ans.extend( [ x[:] for x in intervals[1:] ]  )
                return ans
            else: #New interval ending is after the first interval
                # I came to this logic later and it is same as finding the toBeEnd from the below part
                startToAdd =  newInterval[0]
                toBeEnd = newInterval[1]
                while itrIdx < len(intervals) and toBeEnd >= intervals[itrIdx][0]:
                        itrIdx += 1

                idxToLookForNewIntervalEnding = itrIdx - 1
                ans.append( [startToAdd, max(toBeEnd, intervals[idxToLookForNewIntervalEnding][1]) ]  )
                #Now if anything left in the intervals just apend them
                ans.extend(  [x[:] for x in intervals[itrIdx:]] )
                return ans
                
        else:
            ans.extend([x[:] for x in intervals[0:itrIdx-1]] )
            idxToLook = itrIdx - 1
            startToAdd = None
            toBeEnd = None
            if newInterval[0] <= intervals[ idxToLook ][1]: #This means newInterval starting index falls within the idxToLook interval
                startToAdd = min( newInterval[0], intervals[ idxToLook ][0] )
                toBeEnd = max( newInterval[1], intervals[ idxToLook ][1] ) #eithi toBe means hei pare, naa hei bi pare
            else:
                ans.append( intervals[idxToLook][:] ) #because starting of new inteval is after of idxToLook
                startToAdd = newInterval[0]
                toBeEnd = newInterval[1]
        
            # Till here in this else block we have finalize the starting of the interval in the startToAdd, now we have to check what will be end and till which the toBeEnd will stretch
            if itrIdx == len(intervals): #Everything is over we can appen the startToAdd and toBeEnd interval
                ans.append( [startToAdd, toBeEnd] )
                return ans
            else:
                while itrIdx < len(intervals) and toBeEnd >= intervals[itrIdx][0]:
                    itrIdx += 1

                idxToLookForNewIntervalEnding = itrIdx - 1
                ans.append( [startToAdd, max(toBeEnd, intervals[idxToLookForNewIntervalEnding][1]) ]  )
                #Now if anything left in the intervals just apend them
                ans.extend(  [x[:] for x in intervals[itrIdx:]] )
                return ans


# intervals = [[1,3],[6,9]]
# newInterval = [2,5]


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]

intervals = [[1,5]]
newInterval = [0,0]

ans  = Solution().insert(intervals=intervals, newInterval=newInterval)
print(ans)