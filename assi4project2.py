m,n= input("enter the M and N \n").split()
M = int(m) ; N = int(n)
for i in range(M):
    if i%2==0:
        for j in range(N):
         print("#*",end='')
    else:
        for j in range(N):
         print("*#",end='')
    print("\n")