import timeit
import os
import random

# N = int(input())
# store = list(map(int, input().split()))

# M = int(input())
# client = list(map(int, input().split()))

# input 1
# N, M = 5, 3
# store, client = [8, 3, 7, 9, 2], [5, 7, 9]
# ouput 1
# no yes yes

# input 2
N, M = 50, 20
store = [73,15,26,59,49,44,8,47,63,74,66,81,67,41,52,45,57,4,51,12,10,37,64,7,48,23,42,18,71,55,36,61,83,82,2,20,94,76,28,58,50,92,79,70,96,19,54,97,40,86]
client = [4,35,20,53,93,6,63,52,21,41,5,77,91,78,79,7,46,39,64,95]
# output 2
# yes no yes no no no yes yes no yes no no no no yes yes no no yes no

# input 3
# N, M = 60, 60
# store = [911,643,184,439,855,981,950,776,519,204,321,47,749,53,851,272,970,270,42,137,523,251,990,171,487,860,796,19,841,46,799,215,333,766,214,709,687,299,334,554,991,396,163,473,869,76,549,128,821,756,703,463,60,283,706,81,314,415,517,375]
# client = [500,923,351,303,489,294,579,708,287,382,137,906,229,788,332,251,862,486,795,638,932,725,573,541,329,177,324,868,710,277,290,909,948,364,87,727,652,497,977,618,532,258,949,632,687,29,735,580,617,770,70,946,569,743,189,388,322,636,61,200]
# output 3
# no no no no no no no no no no yes no no no no yes no no no no no no no no no no no no no no no no no no no no no no no no no no no no yes no no no no no no no no no no no no no no no

'''=== way1. binary search ==='''
def binary_search(target, start, end, arr):
    if start > end:
        return False
    mid = (start + end) // 2 # 괄호가 없으면 우선 순위가 달라짐
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        return binary_search(target, start, mid-1, arr) # -1 자꾸 까먹음..!
    else:
        return binary_search(target, mid+1, end, arr) # +1 자꾸 까먹음..!

start_time = timeit.default_timer()
store = sorted(store)
for target in client:
    if binary_search(target, 0, N-1, store):
        print("yes", end = ' ')
    else: 
        print("no", end = ' ')
print()
end_time = timeit.default_timer()
print(">> binary_search time: ", end_time - start_time)

'''=== way2. set() ==='''
# N = int(input())
# store = set(map(int, input().split())) #!! list 대신 set으로!
# M = int(input())
# client = list(map(int, input().split()))

set_store = set(store)
start_time = timeit.default_timer()
for target in client:
    if target in set_store:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
end_time = timeit.default_timer()

'''=== way3. 계수 정렬(생략) ==='''

'''=== ramdom한 정수를 중복되지 않게 sampling 해주는 함수 ==='''
def make_testcase():
    # input_text: txt 파일에 쓸 내용
    input_list = random.sample(range(1,1000), 60)
    
    input_len = len(input_list)
    
    input_text = 'N = '+ str(input_len) + '\n' + '['
    for i in input_list:
            input_text = input_text + str(i) + ","
    input_text = input_text[:-1] + ']\n'

    #idx_list = [random.randint(0, input_len-1) for _ in range(int(input_len*0.3))]
    # for i in idx_list:
    #     input_list[i] = int(input_list[i] / random.randint(10, 100))

    client_list = random.sample(range(1,1000), 60)
    input_text = input_text + 'M = '+ str(len(client_list)) + '\n' + '['
    for i in client_list:
        input_text = input_text + str(i) + ","
    input_text = input_text[:-1] + ']\n'
    print(input_text)

    # input_set = set()
    # for ele in input_list:
    #     input_set.add(ele)
    # print(len(input_set))

    # 계속해서 input을 만들어주는 text 저장하기
    curdir_path = os.getcwd() + '/CH7 Search/'
    filename = curdir_path + 'p2_input.txt'
    with open(filename, 'w') as file:
        file.write(input_text)