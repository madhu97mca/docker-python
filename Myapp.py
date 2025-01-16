#This code will reads the outside file and displays the contents present inside the file.
try:
    with open('server.txt','r')as file:
        content = file.readlines()
except Exception as e:
    print(e,type(e))
else:
    for line in content:
        print(f'{line.rstrip()}')
