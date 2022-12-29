n=int(input("enter how many nats nums u want to find:"))
if(n<=0):
    print("{} is a invalid input:".fomrat(n))
else:
    print("-"*50)
    print("\t nat nums sum ,squares,cubes")
    print("-"*50)
    print("hello lavi")
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t{}\t\t{}\t{}".format(i,i**2,i**3))
        i=i+1
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("\t{}\t\t{}\t{}".format(s,ss,cs))
        print("-"*50)
























