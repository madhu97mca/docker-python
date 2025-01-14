user_name=input("Enter your name to store in file or enter to proceed")
if user_name:
    with open("user_info.txt","a")as file:
        file.write(user_name + "\n")

show_info=input("Do u want to see all the user names? y/n:")
if show_info == 'y':
    try:
        with open('user_info.txt','r')as file:
            content = file.readlines()
    except Exception as e:
        print(e,type(e))
    else:
        for line in content:
            print(f'{line.rstrip()}')
elif show_info == 'n':
    print(" you choosed no,so no data will be displayed \n GOOD BYE.")
else:
    print("No data present.")