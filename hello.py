n = int(input())
i = 1
while i <= n:
    space = 1
    while space <=n-i:
        print(" ",end="")
        space+=1
    star = 1
    while star<=i:
        print(star,end="")
        star+=1
    star=1
    p=i
    while star<=i-1:
        print(p-1,end="")
        star+=1
        p-=1
    i+=1
    print()


