from typing import List
class Solution:
    #双指针
    def trap(self, height: List[int]) -> int:
        if height == []: return 0
        area = 0
        i = 0
        j = len(height) - 1
        leftMax = height[i]
        rightMax = height[j]
        while i < j:
            print(i,j)
            if height[i] < height[j]:
                if height[i] > leftMax:
                    leftMax = height[i]
                water = leftMax - height[i]
                if water < 0:
                    water = 0
                print("water: %d" % water)
                area += water
                i += 1
            else:
                if height[j] > rightMax:
                    rightMax = height[j]
                    leftMax = height[i]
                water = rightMax - height[j]
                if water < 0:
                    water = 0
                print("water: %d" % water)
                area += water
                j -= 1
            
        return area

if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
