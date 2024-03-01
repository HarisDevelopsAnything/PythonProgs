for n in range(1,51):
    if(n%3==0):
        if(n%5!=0):
            print("{a} - Fizz".format(a=n))
        else:
            print("{a} - FizzBuzz".format(a=n))
    elif(n%5==0):
        print("{a} - Buzz".format(a=n))