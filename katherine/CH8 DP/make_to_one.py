# n = int(input())
# storage = list(map(int, input().split()))
# print(n, storage)

'''
input 1: 4, [1,3,1,5]
output 1: 8

input 2: 10, [11, 6, 12, 3, 4, 1, 18, 2, 17, 16]
output 2: 62

input 3: 20, [2, 9, 14, 17, 26, 21, 1, 22, 4, 10, 23, 15, 13, 25, 6, 20, 5, 3, 12, 24]
output 3: 166

input 4: 15, [1, 100, 1, 1, 1, 100, 1, 100, 100, 1, 1, 100, 100, 100, 1]
output 4: 502
'''

n, storage = 15, [1, 100, 1, 1, 1, 100, 1, 100, 100, 1, 1, 100, 100, 100, 1]
table_DP = [0 for _ in range(n)]
'''my code'''
# table_DP[0] = storage[0]; table_DP[1] = storage[1]; 
table_DP[0] = storage[0];
table_DP[1] = max(storage[0], storage[1]) # dodoong!

for i in range(2,n):
    candidates = []
    # defore max sum
    candidates.append(table_DP[i-1])
    # front + my sum
    '''my code'''
    # for j in range(i-1):
    #     candidates.append(table_DP[j]+ storage[i])
    candidates.append(table_DP[i-2] + storage[i])
    table_DP[i] = max(candidates)

print(table_DP)
print(table_DP[n-1])

'''testcase 생성하기'''

import random
def create_input(min, max, N):
    input_list = random.sample(range(min,max), N)
    print(input_list)

# create_input(1, 20, 10)
# create_input(1, 30, 20)
