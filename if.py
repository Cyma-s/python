# Q1

print("결괏값은 need 이다.")

# Q2

i = 1
sum = 0
while i <= 1000:
    if i % 3 == 0 :
        sum += i
    i += 1

print("3의 배수의 합은 %d이다." % sum)

# Q3
i = 1
while i <= 5:
    print("*"*i)
    i += 1

# Q4

for i in range(1, 101):
    print("{}".format(i))

# Q5

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in score:
    sum += i

mean = sum / len(score)
print(mean)

# Q6

numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)