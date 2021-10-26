n,m=input("please enter m and n \n").split()
M=int(m); N=int(n)


for i in range(M):
    for j in range(N):
        print((i+1)*(j+1),end=" ")

    print("\n")