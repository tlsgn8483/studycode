import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 최대힙 일 경우 -value
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 최대 힙일경우 -heapq
    return result

result = heapsort(([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(result)
# O n log n 계산

