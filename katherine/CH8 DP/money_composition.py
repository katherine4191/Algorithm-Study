# n,m = map(int, input().split()) 
# coins = [0] * n
# table = [10001] * (m + 1) # 0 <= m <= 10000
# for i in range(n):
#     coins[i] = int(input());     table[coins[i]] = 1

# input 1 
n, m = 3, 115
coins = [1, 7, 11]
# ouput 1
14

'''
input 2
n, m = 10, 9668
coins = [50, 46, 80, 85, 66, 28, 95, 22, 99, 7] 
output 2
98

input 3
n, m = 10, 5726
coins = [92, 72, 97, 89, 29, 12, 80, 90, 81, 16]
output 3 
60
'''
table = [10001] * (m + 1) # 0 <= m <= 10000

for coin in coins:
    table[coin] = 1

for coin in coins:
    for step in range(coin, m+1):
            table[step] = min(table[step], table[step-coin] + 1)

if table[m] == 10001:
    print("-1")
else:
    print(table[m])

# print(table)
# print(table[m])

'''testcase 생성하기'''
import random
def create_input(min, max, N):
    input_list = random.sample(range(min,max), N)
    print(input_list)

# create_input(1, 100, 10)
# create_input(1, 10000, 1)

'''Ch3.Greedy의 거스름돈 구하기 문제에서의 정당성'''
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 조합해 다른 해가 나올 수 X 
# 만약, 화폐이 단위가 무작위로 주어졌을 때에 그리디 알고리즘으로 해결할 수 없다. -> 다이나믹, 그래프 알고리즘
# ex) 화폐 종류: 1,7,11로 115원을 만들 때
# 11 10개, 1 5개 -> 그리디 사용시 15개
# 11+7=18이며, 115 = 18*6 + 7 따라서 6*2+1로 13개가 필요하다.