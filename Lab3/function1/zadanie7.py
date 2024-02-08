def List(nums):
    for i in nums:
        if i not in List1:
            List1.append(i)
    return List1

nums = list(map(int, input().split()))
List1 = []
Num = List(nums)
print(Num)