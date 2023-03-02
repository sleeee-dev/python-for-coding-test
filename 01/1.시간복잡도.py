# 시간복잡도
# big O 표기법


# array = [3, 5, 1, 2, 4]
# summary = 0

# for x in array:
#   summary += x
# print(summary)
# 시간복잡도 : O(N)


import time
start_time = time.time()

array = [3, 5, 1, 2, 4]

for i in array:
  for j in array:
    temp = i * j
    print(temp)

end_time = time.time()
print("time:", end_time - start_time)
# 시간복잡도 : O(N^2)

# 알고리즘 설계시 주의할 것 : 시간제한 (수행시간 요구사항)
# 이것때문에 시간복잡도를 알아두라는것

# python이 1초에 2천만번 정도의 계산을 한다고 가정
# 시간제한이 1초인 문제인 경우
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있다.

# 수행시간 측정을 위한 함수
# 문제를 풀 때 다음 코드를 활용하면서 수행시간에 대한 감 잡아가기

# import time
# start_time = time.time() # 측정 시작
# # 프로그램 소스코드
# end_time = time.time() # 측정 종료
# print("time:", end_time - start_time) # 수행 시간 출력