# task 1
for i in range (0,5):
    print(i+1, (i+1)*'0')

# task 2
a=0
for i in range(1,11):
    b=int(input('введите число'))
    if b==5:
        a=a+1
    else:
        a=a
print(a)

# task 3
sum = 0
for i in range(1,101):
     sum+=i
print(sum)

# task 4

for i in range(1,11):
    a*=i
print(a)

# task 5

integer_number = 2129

print(integer_number%10,integer_number//10)

while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

# task 6

b=0
e=0
a=123
while a>0:
    b=a%10
    e=e+b
    a=a//10
print(e)

# task 7

b=0
e=1
a=123456
while a>0:
    b=a%10
    e=e*b
    a=a//10
print(e)

# task 8

a = 123456780897565
while a>0:
    if a%10 == 5:
        print('Yes')
        break
    a = a//10
else:
    print('No')

# task 9

a=12345678087565
b=0
while a>0:
    if a%10>b:
       b=a%10
    else:
        b=b
    a = a//10
print(b)

# task 10

b=0
a = 523454
while a>0:
    if a%10 == 5:
        b=b+1
    else:
        b=b
    a=a//10
print(b)
