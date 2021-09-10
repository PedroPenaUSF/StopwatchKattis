n = int(input())
i = 0
time = 0
if n % 2 != 0:
    while i < n:
        input()
        i = i + 1
    print('still running')
else:
    while i < n:
        a = int(input())
        b = int(input())
        time = time + b - a
        i = i + 2
    print(time)
