ans = 0
matches = 0
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
for i in range(len(objects)): #len = 11
    for j in range(i + 1, len(objects)):    #от
        if objects[j] is objects[i]:
            matches += 1
    if matches == 0:
        ans += 1
    matches = 0
print(ans)