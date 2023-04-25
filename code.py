a=int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplication(a,b):
    return a*b

def exponential(a,b):
    return a**b

print("Select operation:\n 1.add\n 2.subtract\n3.division\n 4.multiplication\n 5.exponential")

select=int(input("Enter operation which you want to perform(1,2,3,4,5): "))

if select==1:
    print (a, "+", b, "=" ,add(a,b))

elif select==2:
    print (a, "-", b, "=" ,subtract(a,b))

elif select==3:
    print (a, "/", b, "=" ,division(a,b))

elif select==4:
    print (a, "*", b, "=" ,multiplication(a,b))

else:
    print (a, "**", b, "=" ,exponential(a,b))
