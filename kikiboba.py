word = str(input())

kNum = 0
bNum = 0

for i in word:
    if i == "k":
        kNum += 1
    if i == "b":
        bNum += 1

if bNum > kNum:
    print("boba")
elif kNum > bNum:
    print("kiki")
elif kNum == 0 & bNum == 0:
    print("none")
else:
    print("boki")
