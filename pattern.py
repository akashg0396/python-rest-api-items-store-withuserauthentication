n = int(input())
n2=n//2
n1=n-n2

for row in range(1,n1+1):
    for space in range(n1-row):
        print(" ",end="")
    for star in range(2*row-1):
        print("*",end="")
    print()
 
for row in range(1,n2+1):
    for space in range(row):
        print(" ",end="")
    for star in range(n2-row+1):
        print("*",end="")
    for star in range(n2-row):
        print("*",end="")
    print()
    