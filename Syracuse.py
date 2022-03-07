
N=int(input("Enter le nombre entier N= "))
n=int(input("Le numéro de la suite que vous souhaitez n= "))
print(N)
for i in range(1,n+1):
    if N%2==0:
        N=N//2
    else:
        N=3*N+1
    print(N)