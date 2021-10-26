need = list(map(int,input().split()))
heights = list(map(int,input().split()))
N=need[0]
M=need[1]

def find(h,arr):
    sum = 0
    for v in arr:
        if v > h:
            sum+=v-h
    return sum
def solution(n,m,arr):
    answer = 0
    start = 0
    end = max(arr)
    while start<=end:
        mid = (start+end)//2
        sum = find(mid, arr)
        if sum >= m:
            answer=mid
            start = mid+1
        else:
            end = mid-1
    return answer

print(solution(N,M,heights))