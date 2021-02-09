# N, target = input().split()
# arr = list(map(str, input().split()))

N, target = 5, 'Dongbin'
arr = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i+1
    return -1

idx = sequential_search(int(N), target, arr)
if idx > 0:
    print("찾고자 하는 문자열은 " + str(idx) + "번째에 있습니다.")
else:
    print("찾고자 하는 문자열이 없습니다.")

'''
5 Dongbin
Hanul Jonggu Dongbin Taeil Sangwook
'''

# N, target = list(map(int, input().split()))
# arr = list(map(int,input().split()))

N, target = 10, 7
arr=[1, 2, 5, 7, 9, 11, 13, 15, 17, 19]

def binary_search(target, start, end, arr):
    if start > end:
        return -1
    mid = start+end // 2
    if target < arr[mid]:
        return binary_search(target, start, mid-1, arr)
    elif target == arr[mid]:
        return mid+1
    else:
        return binary_search(target, mid+1, end, arr)

idx = binary_search(target, 0, N-1, arr)
if idx > 0:
    print("찾고자 하는 숫자는 " + str(idx) + "번째에 있습니다.")
else:
    print("찾고자 하는 숫자가 없습니다.")

'''
10 7
1 2 5 7 9 11 13 15 17 19

10 7
1 3 5 6 9 11 13 15 17 19
'''