#sum of number stored in list
numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
for i in numbers:
    sum = sum + i

print(sum)

#range function
for _ in range(4):
    print(tuple(range(5)))

#iterate through a list using indexing
genre = ['pop','rock','jazz']

for i in range(len(genre)):
    print('i like', genre[i])

for i in range(0,10,2):
    print(i,i**2)

#pattern through for loop
for num in range(1,4):
    for i in range(num):
        print(num, end= ' ')
    print()

for row in range(1,6):
    for col in range(1,row+1):
        print(col, end=" ")
    print('')

for row in range(0,9):
    for col in range(row,1,-1):
        print(col, end=' ')
    print(' ')

'''
1
2 3 4
5 6 7 8 9
'''
row = 4
temp = 0
stop = 1
for row in range(0,row):
    for col in range(0, stop):
        temp = temp+1
        print(temp, end= ' ')
    print('')
    stop = stop+2


'''
1
3  2
6  5  4
10 9  8 7
'''
print('New programsssssssssssssssss ####################')
start = 1
stop = 2
temp = stop
for row in range(2,6):
    for col in range(start, stop):
        temp = temp-1
        print(temp, end= ' ')
    start = stop
    stop = stop + row
    temp = stop
    print('')

rows = int(input('enter no of rows'))
for r in range(1,rows+1):
    for c in range(1,r+1):
        print('#',end=' ')
    print()
for r in range(rows,0,-1):
    for c in range(1,r+1):
        print('#',end=' ')
    print()

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 
'''
value = int(input('enter rows'))
for i in range(row,0,-1):
    for c in range(1,i):
        print(c,end=" ")
    print()

'''
1
2 3
4 5 6
'''
value = int(input('enter rows'))
temp = 0
for i in range(0,row+1):
    for j in range(0,i):
        temp = temp +1
        print(temp, end=' ')
    print()


# pattern
picture = [
 [0,0,0,1,0,0,0],
 [0,0,1,1,1,0,0],
 [0,1,1,1,1,1,0],
 [1,1,1,1,1,1,1],
 [0,0,0,1,0,0,0],
 [0,0,0,1,0,0,0]
]
for i in picture:
 for j in i:
  if j==1:
   print("*", end='')
  else:
   print(' ',end='')
 print()