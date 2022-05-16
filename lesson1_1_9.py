n = int(input())
some_list = []
i = 0
while len(some_list) < n:
    some_list.append(int(input()))
    i+=1
print(sum(some_list))