n = 5
arr = [0] * n
arr_reversed = []
top = 0
print("Enter sth to start", n, "ints left","top = ", top)
x = int(input())

while x != 0:
    ints = n-1
    arr[top] = x
    top += 1
    n -= 1
    print("Enter an integer", "integers left : ", ints, "top = ", top)
    x = int(input())
    if ints == 0:
        break
print(arr)

for i in range(top-1, -1, -1):
    arr_reversed.append(arr[i])

print(arr_reversed)
