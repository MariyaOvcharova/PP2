def has_33(nums):
    for i in range(0, len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

nums = list(map(int, input().split()))
Num = has_33(nums)
print(Num)