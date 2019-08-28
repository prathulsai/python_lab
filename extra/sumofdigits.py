a=int(input())
sum=0
while(a>0):
    sum=sum+a%10
    a=int(a/10)
print(sum)    
