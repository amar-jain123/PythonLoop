# #print table of 5
# num = int(input('enter the number: '))
# for i in range(1,11):
#     table = num*i
#     print(table)
#chech armstrong number
# num = int(input('enter the number along to print'))
# sum=0
# temp=num
# while temp>0:
#     digit = temp%10
#     sum = sum + digit**3
#     temp= temp//10
# if num==sum:
#     print('yes it is armstrong no')
# else:
#     print('sorry')

# print armstrong number
# num = int(input('enter the number along to print'))
# for i in range(100,num+1):
#     temp=i
#     sum=0
#     while temp > 0:
#         digit = temp % 10
#         sum = sum + digit ** 3
#         temp= temp // 10
#
#     if i ==sum:
#         print(i)

# print square of number between a and b
# a = int(input('print the value of a or lower'))
# b = int(input('print the values of b or upper'))
# for i in range(a,b+1):
#     square = i**2
#     print(square)

# print sequence of number with given step size and boundary values

a = int(input('enter the 1st value'))
b = int(input('enter the 2nd value'))
step =0
count = 0
number = a
while a > 0:
    a = a // 10
    count = count + 1
for i in range(number, b+1, count):
    print(i)
