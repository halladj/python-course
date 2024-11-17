try:
    fout = open('relativity', 'r')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')
except:
    print("Unsupported Syntax OR Operation")
    