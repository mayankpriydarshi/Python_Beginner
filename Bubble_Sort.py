import re


def bubble_sort():
    nums_input = input(" enter array: ")
    nums = [int(m) for m in re.split(r'[,\s]+', nums_input)]
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


sorted_nums = bubble_sort()
print("Sorted array:", sorted_nums)
