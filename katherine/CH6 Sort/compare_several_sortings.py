# selection sort 선택 정렬
# 가장 작은 것을 선택해 차례대로 맨 앞의 데이터와 바꾸는 정렬 방법
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        #print("sorting ... ",arr)
    return arr

''' output
sorting ...  [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]
sorting ...  [0, 1, 2, 7, 3, 5, 6, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 7, 5, 6, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# Insertion sort 삽입 정렬
# 특정한 값을 적절한 위치에 삽입하는 정렬 방법(그 위치 앞까지는 이미 정렬되어 있음)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]: # 해당 데이터의 위치 자동 갱신 가능
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else: 
                break
        #print("sorting ... ",arr)          
    return arr 

''' output
sorting ...  [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorting ...  [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
sorting ...  [0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
sorting ...  [0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
sorting ...  [0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# quick sort 퀵 정렬
# pivot을 사용하여 왼쪽부터 pivot보다 큰 데이터를 찾고, 오른쪽부터 pivot보다 작은 데이터를 찾아
# 큰 데이터와 작은 데이터를 찾아 위치를 서로 교환하는 정렬 방법
def quick_sort(pivot, end, arr):
    if pivot >= end:
        return    
    
    left, right = pivot + 1, end
    
    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > pivot and arr[pivot] <= arr[right]:
            right -= 1

        if left > right: # 두 값이 엇갈린 경우 작은 데이터(right)와 pivot 교체
            arr[pivot], arr[right] = arr[right], arr[pivot]
            #print("sorting ... "arr)
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 현재는 arr[right]에 pivot 값이 존재, pivot은 배열의 앞 부분을 의미
    quick_sort(pivot, right - 1, arr) 
    quick_sort(right + 1, end, arr)
    return arr

''' pivot이 바뀌는 과정
sorting ... [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
sorting ... [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
sorting ... [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ... [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ... [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
sorting ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# counting sort 계수 정렬
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담아 정렬하는 방법
def counting_sort(arr):
    count_arr = [0 for _ in range(max(arr)+1)]

    for val in arr:
        count_arr[val] += 1
    
    arr = []
    for i in range(len(count_arr)):
        while count_arr[i]:
            arr.append(i)
            count_arr[i] -= 1
            
    return arr


def main():
    unsorted = [5,7,9,0,3,1,6,2,4,8]
    print("selection_sort",selection_sort(unsorted))
    
    unsorted = [7,5,9,0,3,1,6,2,4,8]
    print("insertion_sort", insertion_sort(unsorted))

    unsorted = [7,5,9,0,3,1,6,2,4,8]
    print("quick_sort", quick_sort(0, len(unsorted)-1, unsorted))
    
    unsorted = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    print("counting_sort", counting_sort(unsorted))

main()
