# Q1

def is_odd(num):
    if num % 2 == 0:
        print("짝수")
    else :
        print("홀수")

# Q2

def mean(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum / len(arg)

print(mean(1, 2, 3))

# Q3

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)

# Q4

print("출력 결과가 다른 것은 3이다.")

# Q5

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

# Q6

user = input("저장할 내용을 입력하세요 : ")
f = open("test.txt", 'a')
f.write("\n")
f.write(user)
f.close()

# Q7

f = open("test.txt", "r")
line = f.read()
f.close()
line = line.replace("java", "python")
f = open("test.txt", "w")
f.write(line)
f.close()