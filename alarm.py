h,m=map(int,input().split())

if m>=45:
    print(h,m-45)
else:
    print(h-1,m+15)#60과 45차이 15