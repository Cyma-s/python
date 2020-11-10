# 별 찍기 -5

num = int(input())
i = 1
while i <= num:
    if i < num :
        print(" "*(num-i), end = '')
        print("*"*(2*i-1))
    else :
        print(" "*(num-i), end = '')
        print("*"*(2*i-1), end = '')
    i += 1