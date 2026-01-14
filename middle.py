n=int(input("Enter a number: "))
t=n
nl=0
while t>0:
    nl=nl+1
    t=int(t/10)
if nl>=4:
        nl=int(nl/2)
        c=0
        while n>0:
            r=n%10
            if c==nl:
                mo=r
            elif c==(nl-1):
                mt=r
            n=int(n/10)
            c=c+1
        p=mo*mt
        print("\nproduct of mid digits("+str(mo)+"*"+str(mt)+")= ",p)
else:
        print("\nit's not a 4 or more than 4 digit number")