import sys

str_nums = sys.argv[1]
list_nums = [int(x) for x in str_nums.split(',')]

i = 0

print(list_nums)

while i < len(list_nums):
    j = 0

    while j < len(list_nums)-i-1:
        if list_nums[j] < list_nums[j+1]:
            list_nums[j], list_nums[j+1] = list_nums[j+1], list_nums[j]
        j += 1
    i += 1

print(list_nums)
