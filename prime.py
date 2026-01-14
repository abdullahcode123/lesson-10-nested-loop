lower=int(input("Enter lower number: "))
higher=int(input("Enter higher number: "))
print("Prime numbers between ",lower," to ",higher,"is : ")
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
                print(num)
  