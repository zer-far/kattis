X = int(input())
N = int(input())
P = X
for i in range(0, N):
    P += X - int(input())
print(P)
