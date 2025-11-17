class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        itrIdx = 0
        insertAfterAllEnds = True #This flag is not needed, because byComparaing itrIdx with len(intervals) we can decide this
        tempStart = None
        tempEnd = None
        #Finding the index where the starting of newInterval will come
        while itrIdx < len(intervals):
            if newInterval[0] < intervals[ itrIdx ][0]:
                tempStart = newInterval[0]
                insertAfterAllEnds = False
                # tempEnd = newInterval[1] #The below logic i missed for first test case in the examples
                break
            elif (newInterval[0] > intervals[ itrIdx ][0] and newInterval[0] <= intervals[ itrIdx ][1] ):
                tempStart = intervals[ itrIdx ][0]
                insertAfterAllEnds = False
                #The below logic i missed for first test case in the examples
                # This is needed because as first index is within the current itrIdx interval, so the potential end can be max of them, think this 
                # tempEnd = max( newInterval[1],  intervals[ itrIdx ][1] ) 
                itrIdx += 1
                break
            else:
                ans.append( intervals[itrIdx][:] ) #Deep copy

            itrIdx += 1
        print("after deciding tempStart", tempStart, itrIdx)
        if insertAfterAllEnds:
            # THe new interval will be after all the earlier intervals
            ans.append( newInterval[:] )
            return ans

        tempEnd = None
        #Now we will find the tempEnd for the tempStart interval
        while itrIdx < len(intervals):
            if tempEnd > intervals[ itrIdx ][1]:
                continue
            elif tempEnd < intervals[ itrIdx ][0]:
                break
            elif (tempEnd >= intervals[ itrIdx ][0] and tempEnd <= intervals[ itrIdx ][1] ):
                tempEnd = intervals[ itrIdx ][1]
                itrIdx += 1
                break
            else:
                ans.append( intervals[itrIdx][:] )

            itrIdx += 1
        print("after deciding tempEnd", tempEnd, itrIdx)
        #We will append the newly decided pair
        ans.append( [tempStart, tempEnd] )
        #Now if there is any left indexes we will append them

        while itrIdx < len(intervals):
            ans.append( intervals[itrIdx][:] )
            itrIdx += 1
        return ans

intervals = [[1,3],[6,9]]
newInterval = [2,5]
ans  = Solution().insert(intervals=intervals, newInterval=newInterval)
print(ans)