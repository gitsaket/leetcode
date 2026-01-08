def prefiex_sum(nums):
    sums = [0]
    for i in nums:
        if i is not 0:
            sums.append(sums[-1] + i)
    return sums


nums = [0, 2, 4, 1, 3, 5]
r = prefiex_sum(nums)
print(r)  # Expected output: [2, 6, 7, 10, 15]
