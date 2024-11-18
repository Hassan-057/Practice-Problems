# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):
    between78 = False
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 7:
            between78 = True
        elif between78 == False:
            sum += nums[i]
        elif nums[i] == 8: 
            between78 = False
    return sum