import sys
import heapq
input = sys.stdin.readline
# 우선 순위 큐 라이브러리 활용한 힙 정렬 구현 예제

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
n = int(input())
arr = []

for i in range (n):
    arr.append(int(input()))
res = heapsort(arr)

for i in range(n):
    print(res[i])