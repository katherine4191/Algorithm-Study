# input
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# method 1
#arr = [27, 15, 12, 123, 32, 1, 34, 2, 11, 87, 4, 17, 88]
arr.sort(reverse=True)
print(arr)

# method 2
#arr = [27, 15, 12, 123, 32, 1, 34, 2, 11, 87, 4, 17, 88]
arr = sorted(arr, reverse = True)
print(arr)

'''
3
15
27
12
'''
