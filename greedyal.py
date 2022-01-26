N = int(input())
A = N//5
N%=5
while A>=0:
    if N%3 == 0:
        B = N//3
        N = N%3
        break
    A-=1
    N+=5
print((N==0) and (A+B) or -1)