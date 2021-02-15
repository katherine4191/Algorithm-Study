import timeit

# input
# N, M = map(int, input().split())
# rice_cakes = list(map(int, input().split()))

# input 1
# N, M = 4, 6
# rice_cakes = [19, 15, 10, 17]
# answer:15

# input 2
# N, M = 50, 456
# rice_cakes = [693, 124, 802, 928, 882, 939, 375, 944, 810, 860, 310, 110, 851, 433, 888, 957, 574, 320, 673, 389, 
# 594, 807, 809, 946, 949, 138, 688, 136, 581, 398, 649, 225, 188, 301, 743, 299, 623, 220, 643, 767, 588, 183, 551, 
# 264, 184, 547, 376, 766, 811, 162]
'''절단기에 설정할 수 있는 높이의 최댓값:  872
>> sequential_search time:  0.0007, >> recursive_binary_search time:  0.0003, >> while_binary_search time:  0.0003
'''

# input 3
N, M = 200, 1357
rice_cakes = [273, 20, 157, 49, 24, 224, 175, 193, 169, 153, 141, 297, 258, 287, 268, 154, 211, 185, 113, 294, 129, 117, 242, 91, 
122, 106, 215, 292, 271, 188, 56, 167, 256, 63, 172, 206, 213, 51, 249, 146, 54, 124, 97, 198, 264, 200, 197, 156, 209,
13, 252, 62, 152, 236, 27, 207, 160, 277, 10, 176, 241, 223, 46, 274, 205, 262, 22, 291, 293, 132, 11, 253, 41, 283, 
199, 110, 126, 36, 71, 105, 220, 87, 231, 31, 171, 128, 263, 270, 30, 95, 281, 183, 155, 260, 216, 135, 44, 257, 276, 
104, 254, 279, 217, 12, 299, 55, 149, 138, 58, 125, 246, 266, 66, 201, 75, 85, 57, 77, 229, 101, 133, 21, 35, 161, 240,
286, 131, 290, 99, 130, 88, 184, 261, 247, 83, 151, 84, 238, 81, 221, 267, 265, 89, 173, 123, 245, 79, 26, 102, 225, 
278, 219, 186, 144, 68, 166, 180, 120, 162, 118, 52, 25, 139, 45, 50, 43, 163, 17, 86, 255, 168, 140, 181, 28, 96, 53,
112, 233, 109, 70, 237, 196, 248, 80, 232, 159, 111, 100, 275, 194, 78, 251, 272, 295, 76, 94, 289, 174, 47, 202]
'''절단기에 설정할 수 있는 높이의 최댓값:  240
>> sequential_search time:  0.0011, >> recursive_binary_search time:  0.0005, >> while_binary_search time:  0.0006
'''
# answer = 240

'''sequential_search'''
def sequential_search(arr):
    max_H = max(arr)
    while max_H > 0:
        total = 0
        for ele in arr:
            if ele > max_H:
                total += ele - max_H
        if total >= M:
            print("절단기에 설정할 수 있는 높이의 최댓값: ", max_H)
            break;
        max_H -= 1
            
'''%% 입력의 범위가 최대 10억까지의 정수이므로 시간 초과를 받는다.'''  
start_time = timeit.default_timer()
sequential_search(rice_cakes)
end_time = timeit.default_timer()
print(">> sequential_search time: ", format(end_time - start_time, ".4f"))

'''binary_search'''
def binary_search(ans, arr, minH, maxH):
    global result
    if minH > maxH:
        return -1
    midH = (minH + maxH) // 2
    total = 0
    for ele in arr:
        if ele > midH:
            total += ele - midH
    if total >= ans:
        result = midH
        return binary_search(ans, arr, midH+1, maxH)
    elif total < ans:
        return binary_search(ans, arr, minH, midH-1)

start_time = timeit.default_timer()
result = 0
binary_search(M, rice_cakes, 0, max(rice_cakes))
print("절단기에 설정할 수 있는 높이의 최댓값: ", result)
end_time = timeit.default_timer()
print(">> recursive_binary_search time: ", format(end_time - start_time, ".4f"))

# solution: 반복문을 사용

minH, maxH = 0, max(rice_cakes)
result = 0
start_time = timeit.default_timer()
while(minH <= maxH):
    midH = (minH + maxH) // 2
    total = 0
    for rice_cake in rice_cakes:
        if rice_cake > midH:
            total += rice_cake - midH
    if total >= M:
        result = midH
        minH = midH + 1
    else:
        maxH = midH - 1
print("절단기에 설정할 수 있는 높이의 최댓값: ", result)
end_time = timeit.default_timer()
print(">> while_binary_search time: ", format(end_time - start_time, ".4f"))


import random
def create_input(min, max, N, answer):
    input_list = random.sample(range(min,max), N)
    input_len = len(input_list)
    print(input_len, answer)
    print(input_list)

#create_input(10, 300, 200, 1357)