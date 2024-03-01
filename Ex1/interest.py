print("Do you want to calculate simple interest or compound interest?")
ch= int(input("1-simple, 2-compound")[0])
if(ch==1):
    p=float(input("Enter the principal amount: "))
    t=int(input("Enter the time period in years: "))
    r=float(input("Enter the rate of interest: "))
    si=p*t*r/100
    print("Simple interest is: {a}".format(a=si))
elif(ch==2):
    p=float(input("Enter the principal amount: "))
    t=int(input("Enter the time period in years: "))
    r=float(input("Enter the rate of interest: "))
    n=int(input("Enter the number of times interest was applied: "))
    ci=p*((1+(r/n)/100)**(n*t))
    print("Compound interest is: {a}".format(a=ci))
else:
    print("Invalid choice!")