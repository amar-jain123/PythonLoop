# sentence = input('Enter a string----------')
# sen = sentence.split()
# print(sen)
# # sen.sort()
# for i in sen:
#     for j in i:
#         if sen[j]>sen[i]:
#             temp = sen[j]
#
#
# for word in sen:
#     print(word)

# while loop.......
# print 10 natural number
num = int(input('enter the numbers to print'))
i = 0
while i<num:
    print(i)
    i = i + 1

#print num in reverse
i = int(input('enter the numbers to print: '))
while i >= 0:
    i =  i - 1
    print(i)

# 10 odd natural no
max = int(input('enter maximum number: '))
i = 1
while i<= max:
    if i%2!=0:
        print('odd numbers are',i)
    else:
        print('even numbers are',i)
    i = i + 1

# print natural number to N  value of N From the user
n = int(input('enter the maximum number u want: '))
i = 0
while i < n:
    print(i)
    i = i + 1

# print natural number to N value of N from user and sum of the numbers
n = int(input('enter the maximum number u want: '))
i = 0
sum=0
while i < n:
    print(i)
    i = i + 1
    sum = sum + i
print("sum of N numbers",sum)

# sum of first N odd natural numbers
n = int(input('enter the maximum no'))
i = 1
sum = 0
while i < n*2:
    if i%2 !=0:
        print((i))
    i = i + 1
    sum = sum + i
print('sum of N ODD no is: ',sum)

# calculate factorial of numbers
num = int(input(('enter the value :  ')))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print(fact)