nums = [2, 5, 5, 8]

nums_iter = iter(nums)
print(next(nums_iter))

for num in nums_iter:
    print(num)

#все числа 

class mYnums:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a 
        self.a += 1
        return x
    
MyN = mYnums()

# for NN in MyN:
#     print(NN)

for i in range(100):
    print(i)


class mYnums1:
    def __init__(self):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.start = 1
        return self
    def __next__(self):
        if self.start>self.stop:
            return StopIteration
        z = self.start
        self.start += 1
        return z
    
MyN1 = mYnums1(5, 12)

for NN in MyN1:
    print(NN)
