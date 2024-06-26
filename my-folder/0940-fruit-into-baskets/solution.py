class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits)==1:
            return 1
        max_fruits=0
        count=collections.Counter()
        left=0
        count[fruits[left]]+=1
        for right in range(1,len(fruits)):
            count[fruits[right]]+=1
            while len(count) >2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            max_fruits=max(max_fruits,right-left+1)
        return max_fruits

