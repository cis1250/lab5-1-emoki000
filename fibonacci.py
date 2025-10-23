#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def user_input():
     term=  int(input("how many terms of the fibonacci sequence do you want?"))
     if term <= 0:
        print("enter a positive number")
        term=  int(input("how many terms of the fibonacci sequence do you want?"))
     return term

def fibonacci(term):
    list =[]
    a=0
    b=1
    for x in range(term):
        list.append(a)
        a, b = b ,a+b
    return list

def main():
    while True:
     term=user_input()
     break
    result = fibonacci(term)
    print(result)


main()
