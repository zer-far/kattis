lst = []
N = int(input())

for _ in range(0, N):
    lst.append(str(input()))
for i in range(0, N, 2):
    print(lst[i])
