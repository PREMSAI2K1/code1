n=int(input())
while True:
    rev=int(str(n)[::-1])
    if rev==n:
        print(n)
        break 
    n=n+1