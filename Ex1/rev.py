from sys import argv as arg
a= int(arg[1][:5])
rev=0
rev+=a%10
a=a//10
rev=rev*10+a%10
a=a//10
rev=rev*10+a%10
a=a//10
rev=rev*10+a%10
a=a//10
rev=rev*10+a%10
print(rev)
