def running_total(nums):
	running_totals = []
	for idx, num in enumerate(nums):
		running_totals.append(num + sum(nums[:idx]))
	return running_totals

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True