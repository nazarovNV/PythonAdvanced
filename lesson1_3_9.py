def closest_mod_5(x):
    i = x
    while i % 5 != 0:
        i = i + 1
    return i

print(closest_mod_5(21))