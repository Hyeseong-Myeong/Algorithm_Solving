import sys
input = sys.stdin.readline 
N, T  = input().split()
N = int(N)
T = int(T)


#입력 및 상대 거리로 절대 위치 추출
location = [0 for _ in range(N)]
sum = 0
for i in range(0,N):
    name, tn = input().split()
    loc_temp = (sum + int(tn)) % T
    location[i] = (loc_temp, name)
    sum += int(tn)

location.sort()

# 사용 가능 여부 산출
available = []
for i in range(N):
    if (location[i][0] == 0) and location[N - 1][0] >= T - 1000:
        available.append(location[i][1])
    else:
        if location[i][0] - location[i - 1][0] <= 1000 and location[i][0] - location[i - 1][0] >= 0:
            available.append(location[i][1])

available.sort()

if len(available) == 0:
    print(-1)
else:
    result = ' '.join(available)
    print(result)