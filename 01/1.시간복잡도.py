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


# <Tip> 입출력 방식이 느릴때 고민해 볼 점
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 그런데 rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 
# 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있다.
# 즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없다.
# 참고로 이름이 꽤 길기 때문에 input = sys.stdin.readline을 맨 처음에 함으로써 쓰면 편하다.
# import sys 도 해줘야함