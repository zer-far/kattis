i = int(input())

if i == 1:
    l = int(input())
    w = l
    h = 3
elif i == 2:
    w = int(input())
    l = int(input())
    h = 3
else:
    w = int(input())
    l = int(input())
    h = int(input())

blocks = (w*h*2 + l*h*2 + w*l) - (h*4 + w*2 + l*2) + 4

print(blocks)
