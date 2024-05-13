numbers = [1,2,3,4,5,6]

def log_pairs(nums):
    for num in nums:
        for other_num in nums:
            print(num,other_num)

log_pairs(numbers)