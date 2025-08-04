print("hello world")

for i in range(1, 101):
    
    if i % 3 == 0 and i % 5 == 0:
        print ("Fizz Bizz number")
    elif i % 3 == 0:
        print("Fizz Number ")
    elif i % 5 == 0:
        print ("Buzz Number")
    else:
        print(i)