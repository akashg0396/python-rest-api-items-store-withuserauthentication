def isSafe(row,col,solution,n):

    i = row-1
    while i>=0:
        if solution[i][col] == 1:
            return False
        i-=1

    i = row-1
    j = col-1
    while i>=0 and j>=0:
        if solution[i][j] == 1:
            return False
        i-=1
        j-=1

    i = row-1
    j = col+1
    while i>=0 and j<n:
        if solution[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def printpathhelper(row,n,solution):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(solution[i][j],end=' ')
        print()
        return
    for col in range(n):
        if isSafe(row,col,solution,n):
            solution[row][col] = 1
            printpathhelper(row+1,n,solution)
            solution[row][col] = 0
    return

def printpath(n):
    solution = [[0 for i in range(n)] for j in range(n)]
    printpathhelper(0,n,solution)



n = int(input())
printpath(n)
