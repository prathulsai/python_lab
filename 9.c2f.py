while(1):
    print("enter ur choice\n1.celsius to fahrenheit\n2.fahrenhiet to celsius\n3.exit")
    a=int(input())
    if(a==1):
        c=int(input("enter celsius"))
        print(c/5*9+32)
    if(a==2):
        f=int(input("enter fahrenheit"))
        print((f-32)/9*5)
    if(a==3):
        break