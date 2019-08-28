a=input().split()
a[0]=int(a[0])
a[1]=int(a[1])
a[2]=int(a[2])
a.sort()
if (a[2]**2==a[1]**2+a[0]**2):
    print("right angled")
else:
    print("not right angled")