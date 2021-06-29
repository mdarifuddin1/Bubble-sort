# Happy coding ,code by Md Arif uddin
# This example of Bubble Sort code 
# coding time 1:28 Am ,date 6/30/2021

def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                print(nums)

nums = [14,3,81,6,7,2,22]
sort(nums)

print(nums)

"""
This code output
[3, 14, 81, 6, 7, 2, 22]
[3, 14, 6, 81, 7, 2, 22]
[3, 14, 6, 7, 81, 2, 22]
[3, 14, 6, 7, 2, 81, 22]
[3, 14, 6, 7, 2, 22, 81]
[3, 6, 14, 7, 2, 22, 81]
[3, 6, 7, 14, 2, 22, 81]
[3, 6, 7, 2, 14, 22, 81]
[3, 6, 2, 7, 14, 22, 81]
[3, 2, 6, 7, 14, 22, 81]
[2, 3, 6, 7, 14, 22, 81]
[2, 3, 6, 7, 14, 22, 81]

"""

