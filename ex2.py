c = input("Enter your celsius: ")
while c.isdigit() == False: 
    c = input("Enter your celsius: ")
print(int(c) + 32)