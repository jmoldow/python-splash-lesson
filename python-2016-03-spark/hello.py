x = input("First number: ")
y = input("Second number: ")
print x, "+", y, "==", x+y


x = input("First number: ")
y = input("Second number: ")
op = raw_input("+, -, *, or / : ")
if op == "+":
    print x + y
elif op == "-":
    print x - y
elif op == "*":
    print x*y
elif op == "/":
    print x/y
else:
    print "Error"
