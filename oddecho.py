lst = []
N = int(input())

for i in range(0, N):
    ele = str(input())
    lst.append(ele)
for i in range(0, N, 2):
    print(lst[i])
