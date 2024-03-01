inp= input('Enter the temperature in the format: n:C/n:F')
degree= int(inp[:len(inp)-2])
conv= 0 if inp[len(inp)-1:] == "C" else (1 if inp[len(inp)-1:] == "F" else 2) 
if conv==0:
    f= degree*9/5+32
    print("{0} degree celsius= {1} degree fahrenheit".format(degree,f))
elif conv==1:
    c= (degree-32)*5/9
    print("{0} degree fahrenheit = {1} degree celsius".format(degree,c))
else:
    print("Invalid formatting!")
    