class TriChetire:
    def __init__(self, start, n):
        self.start = start
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.n:
            raise StopIteration
        k = self.start
        self.start += 1
        if k%3==0 and k%4==0:
            return k
    
start = 1
n = int(input())
mm = TriChetire(start, n)
list = []

for num in mm:
    if isinstance(num, int):
        list.append(num)
   
print(', '.join(map(str, list)))