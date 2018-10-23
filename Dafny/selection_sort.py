import sys

str_nums = sys.argv[1]
list_nums = [int(x) for x in str_nums.split(',')]

print(list_nums)

i = 0
while i < len(list_nums):
    min_index = i

    j = i+1
    while (j < len(list_nums)):
        if list_nums[j] < list_nums[min_index]:
            min_index = j
        j += 1

    list_nums[i], list_nums[min_index] = list_nums[min_index], list_nums[i]
    i += 1

print(list_nums)
