m1=int(input("enter rows of 1st matrix : "))
n1=int(input("enter cols of 1st matrix : "))
m2=int(input("enter rows of 2nd matrix : "))
n2=int(input("enter cols of 2nd matrix : "))
if(n1!=m2):
    print("matrix multiplication is not possible")
else:
    a=[]
    a=input().split(" ")
    b=input().split(" ")
    la=len(a)
    lb=len(b)
    for i in range(la):
        a[i]=int(a[i])
    for i in range(lb):
        b[i]=int(b[i])
    c=[]
    for i in range(m1*n2):
        c.append(int(0))
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                c[i*n2+j]=c[i*n2+j]+a[i*n1+k]*b[k*n2+j]
    print(c)