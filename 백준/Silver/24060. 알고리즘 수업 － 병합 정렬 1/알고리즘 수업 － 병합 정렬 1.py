cnt = 0
answer = -1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # 중간 지점
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

def merge(A, p, q, r):
    global cnt, answer, k
    tmp = [0] * (r - p + 1)  # 임시 배열 (1-based 인덱스처럼 사용)
    i, j, t = p, q + 1, 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    for i in range(p, r + 1):
        A[i] = tmp[i - p]
        cnt += 1
        if cnt == k:
          answer = A[i]

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
merge_sort(arr, 1, n)
print(answer)
