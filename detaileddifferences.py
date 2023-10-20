n = int(input())

for i in range(n):
    differences_lst = []
    test_case = []
    for _ in range(2):
        test_case.append(str(input()))

    for j in range(len(test_case[0])):
        if test_case[0][j] == test_case[1][j]:
            differences_lst.append(".")
        else:
            differences_lst.append("*")

    differences = "".join(differences_lst)

    print(f"{test_case[0]}\n{test_case[1]}\n{differences}\n")
