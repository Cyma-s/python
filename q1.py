# Q1

a = 80
b = 75
c = 55
print((a+b+c)/3)

# Q2

n = 13
if n%2 == 1 :
    print("홀수")
else:
    print("짝수")

# Q3

number = "881120-1068234"
print(number[0:6])
print(number[7:14])

# Q4

pin = "881120-1068234"
print(pin[-1])

# Q5

a = "a:b:c:d"
replace_a = a.replace(":","#")
print(replace_a)

# Q6

li = [1,3,5,4,2]
li.sort()
print(li)

# Q7

life = ['Life', 'is', 'too', 'short']
life_string = ' '.join(life)
print(life_string)

# Q8

tu = (1,2,3)
tu = tu + (4,)
print(tu)

# Q9

# 오류는 3번에서 발생한다.
# 딕셔너리의 키 값으로 변하는 값인 리스트를 사용할 수 없기 때문.

# Q10

a = {'A':90, 'B':80, 'C':70}
b = a.pop('B')
print(b)

# Q11

a = [1,1,1,2,2,3,3,3,4,4,5]
st = set(a)
a = list(st)
print(a)

# Q12

a = b = [1,2,3]
a[1] = 4
print(b)

# a와 b 모두 동일한 리스트를 가리키고 있기 때문.