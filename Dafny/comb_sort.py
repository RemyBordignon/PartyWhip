import sys

# To find next gap from current 
def getNextGap(gap): 
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return gap 
  
def combSort(arr): 
    n = len(arr)
    gap = n
    swapped = True

    while gap !=1 or swapped == 1: 
        gap = getNextGap(gap) 
        swapped = False
        for i in range(0, n-gap): 
            if arr[i] > arr[i + gap]: 
                arr[i], arr[i + gap]=arr[i + gap], arr[i] 
                swapped = True


str_nums = sys.argv[1]
list_nums = [int(x) for x in str_nums.split(',')]

i = 0

print(list_nums)
print("sorted: " + combSort(list_nums))