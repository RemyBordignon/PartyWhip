import sys

str_nums = sys.argv[1]
list_nums = [int(x) for x in str_nums.split(',')]

print(list_nums)

curr = 1
while curr < len(list_nums):
	num = list_nums[curr]
	prev = curr - 1
	list_nums[curr] = list_nums[prev]

	while prev >= 0 and list_nums[prev] < num:
		list_nums[prev + 1] = list_nums[prev]
		prev -= 1

	list_nums[prev + 1] = num
	curr += 1

print(list_nums)