'''
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
                '''
# first input the number of rows
rows = int(input())
# outer loop
for i in range(1, rows+1):
    # Inner loop start, stop and step
    for j in range(-1+i, -1, -1):
        print(2**j, end=' ')
    # for new lines
    print('')

# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [i*i for i in a if i%2 == 0]
print(square)

# lambda function map, reduce, filter
square_list = list(map(lambda x: x*x, a))
print(square_list)

