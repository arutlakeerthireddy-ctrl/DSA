'''
Container With Maximum Water
Problem: Given heights of vertical lines, find the maximum amount of water a container can store.
Example:
Input:[1,8,6,2,5,4,8,3,7]
Output:49'''
def container_max_water(heights):
    n=len(heights)
    left=0
    right=n-1
    current_area=0
    maximum_area=0
    while left<right:
        current_area=((right-left)*min(heights[left],heights[right]))
        maximum_area=max(current_area,maximum_area)
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return maximum_area
heights=[1,8,6,2,5,4,8,3,7]
print(container_max_water(heights))#49
    