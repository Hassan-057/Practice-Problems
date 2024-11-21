# Imagine you are given a list called 'nums' containing distinct integers sorted in non-decreasing order, and another integer named 'target'.
# Your task is to find the position of 'target' within 'nums'.
# Should 'target' be present in 'nums', return its array index.
# If 'target' is absent from 'nums', return -1.
# Design your solution to operate with a time complexity of O(log n), leveraging the efficiency of binary search.
 
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: Since 9 is present in 'nums', its index 4 is returned.
 
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: Given 2 does not appear in 'nums', -1 is returned.
 
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All integers in 'nums' are distinct.
# 'nums' is sorted in non-decreasing order.

#This is the change that i am making nothing just the read me and some print statements

def locate_element(nums, target):
    left = 0
    right = len(nums)-1
    print(left,right)
    while(left<=right):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid -1
        else:
            left = mid+1
    print("Nothing is happening")
    return -1