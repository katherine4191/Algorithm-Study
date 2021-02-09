arr = []

# input
n = int(input())
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda grade: grade[1])

for data in arr:
    print(data[0], end=' ')
    
'''
2
홍길동 95
이순신 77
'''