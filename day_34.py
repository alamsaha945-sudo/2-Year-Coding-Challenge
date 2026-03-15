# Find The Runner- score
n=int(input())
arr=map(int,input().split())
un_score=list(set(arr))
un_score.sort()
print(un_score[-2])