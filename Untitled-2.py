def calculator(operation,a,b):
    #operation=["+","*","-","/"]
    #print('enter the operation')
    #operation=input()
   # print('enter a')
   # a=input()
   # a=int(a)
   # print('enter b')
   # b=input()
   # b=int(b)
    if operation =="+":
        print('this operation is the addition','and the result is',a+b)
    elif operation =="*":
        print ('this op is a multiplication','and the result is',a*b)
    elif operation =="-":
        print('this op is a subtraction','and the result is',a-b)
    elif operation =="/":
        print('this op is a division','and the result is',a/b)
    else :
        print('this is not an opeartion')

calculator('*',1,2)