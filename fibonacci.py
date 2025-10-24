#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def user_input():
    while True:
     intut= input("how many terms of the fibonacci sequence do you want?")
     if intut.isdigit():
        term= int(intut)
        if term>0:
            return term
            break
        else:
         print("enter a positive integer")
     else:
        print("enter a valid integers")

def fibonacci(term):
    list =[]
    a=0
    b=1
    for x in range(term):
        list.append(a)
        a, b = b ,a+b
    return list

def main():
    term=user_input()
    result= fibonacci(term)
    print(result)


main()
