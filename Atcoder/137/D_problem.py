import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
job = sorted(AB)
reward_list = []
ans = 0
j = 0
for i in range(1, M + 1):
    while j < N and job[j][0] <= i:
        heapq.heappush(reward_list, -job[j][1])
        j += 1
    if len(reward_list) > 0:
        ans -= heapq.heappop(reward_list)
print(ans)
