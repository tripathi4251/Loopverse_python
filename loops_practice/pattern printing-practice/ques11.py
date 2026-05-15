
#print right side--right angle triangle..


r = 5

for i in range(1, r + 1):

    # Print spaces
    for j in range(r - i):
        print(" ", end=" ")

    # Print stars
    for k in range(i):
        print("*", end=" ")

    print()