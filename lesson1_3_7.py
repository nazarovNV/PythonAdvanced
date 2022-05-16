global stack_num

stack_num = 1


def h():
    global stack_num
    stack_num += 1
    print(12)


def f():
    global stack_num
    stack_num += 1
    g(h)


def g(a):
    global stack_num
    stack_num += 1
    a()


stack_num += 1
g(f)

print('stack_num:', stack_num)  # stack_num: 6