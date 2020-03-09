c = input("Enter the quantity of products: ")
while c.isdigit() == False or int(c) <= 0: 
    c = input("Quantity must be a number and be greater than zero. Enter quantity try again : ")
c = int(c)
products = []
i =1
while i<=c:
    name= input("Enter your name's product {}: ".format(i))
    products.append(name)
    i+=1
key = input("Enter your key :")
if len(list(filter(lambda name: name == key, products))) >0 :
    print("Avaiable")
else:
    print("Out of stock")
