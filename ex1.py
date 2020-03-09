s = input("Enter your string: ")
c = input("Enter your character: ")
print(len(list(filter(lambda char: char == c, list(s)))))