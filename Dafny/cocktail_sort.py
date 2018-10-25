import sys

str_nums = sys.argv[1]
list_nums = [int(x) for x in str_nums.split(',')]

print(list_nums)

start = 0
end = len(list_nums) - 1

while (start < end):
	i = start

	while (i < end):
		if list_nums[i] > list_nums[i+1]:
			list_nums[i], list_nums[i+1] = list_nums[i+1], list_nums[i]
		i += 1

	end -= 1
	i = end

	while (i > start):
		if list_nums[i] < list_nums[i-1]:
			list_nums[i], list_nums[i-1] = list_nums[i-1], list_nums[i]
		i -= 1

	start += 1

print(list_nums)