def calculator(op, num1, num2):
    if   op == "+":
        print(num1,op,num2,"==",num1 + num2)
    elif op == "-":
        print(num1,op,num2,"==",num1 - num2)
    elif op == "*":
        print(num1,op,num2,"==",num1 * num2)
    elif op == "/":
        print(num1,op,num2,"==",num1 / num2)
    elif op == "%":
        print(num1,op,num2,"==",num1 % num2)
    elif op == "//":
        print(num1,op,num2,"==",num1 // num2)
    elif op == "**":
        print(num1,op,num2,"==",num1 ** num2)
    else:
        print("invalid operation")

calculator()
