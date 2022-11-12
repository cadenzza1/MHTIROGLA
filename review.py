import sys
input = sys.stdin.readline

def binary_search(arr,target,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if arr[mid] == target:
        return 1
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분 확인
    else:
        return binary_search(arr,target,mid+1,end)

n = int(input())
arr_n = list(map(int,input().split()))
arr_n.sort()
m = int(input())
arr_m = list(map(int,input().split()))

for i in arr_m:
    print(binary_search(arr_n,i,0,len(arr_n)-1), end = ' ')
