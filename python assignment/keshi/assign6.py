#sort A list given by user
# wash= list(input('enter the list'))
# wash.sort()
# print(wash)
#find greatest number in the list by user
# rash = list(input('enter the list'))
# rash.sort()
# print(rash)
# print(rash[-1])
# calculate sum of integer in the list by user
# main = int(input('enter the elements'))
# lst = []
# for i in range(main):
#     num = int(input('enter the number'))
#     lst.append(num)
# 1# print('sum of list is',sum(lst))

# create list of first N prime no
# num = int(input('enter the value'))
# lst = []
# while num>0:
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
#         lst.append(num)
#     num= num - 1
# print(lst)
# lst.reverse()
# print(lst)

# square of first N natural number
# value = int(input('eneter the value'))
# lst = []
# for obj in range(0,value+1):
#     square = obj**2
#     lst.append(square)
# print(lst)
# indices of given element in a list
# n = int(input('Enter the number which inside the list'))
# listValue =[]
# for temp in range(0,n):
#     value = int(input())
#     listValue.append(value)
#
# print('Entered list by the user',listValue)
# count =0
# for i in range(len(listValue)):
#     print(i, end=' ')
#     print(listValue[i])

# print distinct element along wit the frequency of element
num = int(input('enter the limit of elements'))
lst = []
for i in range(0,num):
    number = int(input('enter elements'))
    lst.append(number)

# [1,2,2,3,1,2]
count=1
visitElement= -1
duplicateList= [0,0,0,0,0,0]
print('list by user',lst)
for i in range(0,len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]== lst[j]:
            count +=1
            duplicateList[j] = visitElement
    if duplicateList[i]!= visitElement:
        duplicateList[i]= count

for i in range(0,len(duplicateList)):
    if duplicateList[i]!= visitElement:
        print(lst[i])






