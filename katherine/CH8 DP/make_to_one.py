#n = int(input())

''' 
input 1:[26]
output: 3 

input 2: [20730, 16465, 27368, 21803, 29081, 23215, 16419, 12244, 16602, 25045]
output 2: 10 13 11 13 14 13 11 11 11 10

input 3: [20730, 16465, 27368, 21803, 29081, 23215, 16419, 12244, 16602, 25045]
output 3: 8 10 9 9 11 11 11 8 11 10 
'''
nums = [8000, 6814, 2553, 3918, 7034, 5806, 5471, 3012, 6986, 5347]

def make_to_one(n):
    arr = [0 for _ in range(n+1)]
    arr[0] = 0; arr[1] = 0; arr[2] = 1; arr[3] = 1; arr[4] = 2; arr[5] = 1

    if n <= 5: 
        print(arr[n])

    operaters = [1,2,3,5]
    for a in range(6, n+1):
        candidates = [30000,30000,30000,30000]
        candidates[0] = arr[a-1] + 1
        if a % 2 == 0:
            candidates[1] = arr[int(a/2)] + 1
        if a % 3 == 0:
            candidates[2] = arr[int(a/3)] + 1
        if a % 5 == 0:  
            candidates[3] = arr[int(a/5)] + 1
        arr[a] = min(candidates)

    print(arr[n], end = ' ')

for num in nums:
    make_to_one(num)

'''testcase 생성하기'''
import random
def create_input(min, max, N):
    input_list = random.sample(range(min,max), N)
    print(input_list)

#create_input(6, 10000, 10)

