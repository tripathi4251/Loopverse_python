
#Print Numbers in an decreasing Sequence (1, 12, 123, 1234, 12345)

r=5
for i in range(r,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()