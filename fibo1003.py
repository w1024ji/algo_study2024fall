t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 1, 0 
    for _ in range(n):
        a, b = b, a+b # temp 생략
    print(a,b)

# f(n) = f(n-1) + f(n-2)
# f(0): 1, 0
# f(1): 0, 1
# f(2): 1, 1
# f(3): 1, 2
# f(4): 2, 3
# f(5): 3, 5

