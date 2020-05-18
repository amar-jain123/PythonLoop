# def sum(a,b):
#     return a+b
#
# a = sum(10,20)
# print('Sum of a and b', a)
#
# def add(a,b):
#     return a + b
# print(add(10,50))

# my name is amar
# string = input('enter the string')
# pangram = 'abcdefghijklmnopqrstuvwxyz'
# s = string.lower()
# lst1 = []
# lst2 = list(pangram)
# for i in pangram:
#     for j in s:
#         if i==j:
#             lst1.append(j)
# if lst1==lst2:
#     print('yes')
# else:
#     print('No')

# def above(*args):
#     return sum(args)
# print(above(1,2,3,4))


def highest_even(list):
    lst = []
    for num in list:
        if num%2==0:
            lst.append(num)
    # for i in range(0,len(lst)):
    #     for j in range(i+1,len(lst)):
    #         if i>j:
    #             j= j+1
    #         else:
    #             i=j
    #             j= j+1
    return max(lst)

print(highest_even([10,12,7,18,122,6,9]))