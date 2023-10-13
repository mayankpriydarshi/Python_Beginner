import re


def insertion_sort():
    nums_input = input("Enter Number: ")
    nums = [int(n) for n in re.split(r'[,\s]+', nums_input)]
    for i in range(len(nums)):
        current = nums.pop(i)
        index = i - 1
        while index >= 0 and nums[index] > current:
            index -= 1
        nums.insert(index + 1, current)
    return nums


sorted_nums = insertion_sort()
print("sorted array: ", sorted_nums)
