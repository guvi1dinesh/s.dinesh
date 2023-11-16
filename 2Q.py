#(2Q) pyramid of numbers from  1 to 20 using for loop

N = 6
i = 0

for row in range(1, N+1):
    for col in range(1, row+1):
        print(i, end=" ")
        i +=1
    print()

