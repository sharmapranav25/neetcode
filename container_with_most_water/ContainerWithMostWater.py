class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0 

        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                length= j - i 
                print(i, j , length)
                bredth= min(heights[i], heights[j])
                print(bredth)
                area= length * bredth
                print(area)
                if area> max_water:
                    max_water= area
        return max_water
        