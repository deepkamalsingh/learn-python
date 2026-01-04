from typing import List
from collections import defaultdict
import heapq

class Solution:


    def mergeLists(self, list1: List[int], list2: List[int]) -> List[int]: 
        finalList = []
        i = 0
        j = 0 
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                finalList.append(list1[i])
                i += 1
            else:
                finalList.append(list2[j])
                j += 1
        return finalList + list1[i:] + list2[j:]

    def minMergeCost(self, lists: List[List[int]]) -> int:

        inf = 9*(10**9)

        totalLists = len(lists)

        dp = [inf for i in range(1 << totalLists)]
        mergedList = [[] for i in range(1 << totalLists)]
        dp[0] = 0 
        for i in range(totalLists):
            dp[1 << i] = 0
            mergedList[1 << i] = lists[i]
        
        for mask in range(1 << totalLists):
            
            submask = mask
            while submask > 0: 
                submask = (submask - 1) & mask
                if submask == 0: 
                    break 

                x = submask
                y = mask ^ submask 

                if x > 0 and y > 0:
                    mergedList[x + y] = self.mergeLists(mergedList[x], mergedList[y])
                    lenX = len(mergedList[x])
                    lenY = len(mergedList[y])
                    dp[x + y] = min(
                        dp[x + y], 
                        dp[x] + 
                        dp[y] + 
                        lenX + 
                        lenY +
                        abs(
                            mergedList[x][(lenX-1)>>1] -
                            mergedList[y][(lenY-1)>>1]
                        )
                    )
            
        return dp[-1]


lists = [[1,3,5],[2,4],[6,7,8]]

print(Solution().minMergeCost(lists))