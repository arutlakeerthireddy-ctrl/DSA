'''Trapping Rain Water
Problem: Given an array representing elevation heights, compute how much rainwater can be trapped.
Example:
Input:
[4,2,0,3,2,5]
Output:9'''

def Trapping_water(heights):
    if len(heights)==0:
        return 0
    left=0
    right=len(heights)-1
    left_max=heights[left]
    right_max=heights[right]
    water=0
    while left<right:
        if left_max<right_max:
            left+=1
            left_max=max(left_max,heights[left])
            water+=left_max-heights[left]
        else:
            right-=1
            right_max=max(right_max,heights[right])
            water+=right_max-heights[right]
    return water
heights=[4,2,0,3,2,5]
print(Trapping_water(heights))

#time complexity=O(n)
#space complexity=O(1)

