class Inventory:

    

    def add(self):

        global manufactur_cost
        manufactur_cost=0
        global monthly_production
        monthly_production=0

        try:
            
            code_product=int(input("Enter product code:"))
            name=input("Enter product name:")
            current_stock=input("please enter current stock:")
            price=float(input("please enter sale price:"))
            manufactur_cost=float(input("enter manufacture cost of the product:"))
            monthly_production=int(input("please enter monthly production:"))

        except:

            print("please enter a valid data type")
            code_product=int(input("Enter product code:"))
            name=input("Enter product name:")
            current_stock=input("please enter current stock:")
            price=float(input("please enter sale price:"))
            manufactur_cost=float(input("enter manufacture cost of the product:"))
            monthly_production=int(input("please enter monthly production:"))



import random
#random module has been imported so that random sold,stock inouts can be genereated.

class Month():
    
    def display(self):

        global monthly_production2
        monthly_production2=0
        coden=int(input("enter product code:"))
        name=input("enter product name:")
        print()
        global sale_price
        global manufacture_cost
        sale_price=float(input("Sale Price:"))
        manufacture_cost=float(input("Manufacture cost:"))
        monthly_production2=int(input("Monthly Production:"))



    def months(self):

        global manufactured
        global sold
        global stock
        manufactured = 0
        sold = 0
        stock = 0
        for i in range(1,13):
            print("Month:",i)

            manufactured=monthly_production2
            print("Manufactured:", manufactured,"units")
            sold=random.randint(manufactured-10,manufactured+10)
            print("Sold:",sold,"units")
            
            stock=random.randint(90,100)
            print("Stock:", stock,"units")
        net = (sold*sale_price) - (manufactured*manufacture_cost)
        print("the total net profit:", "$",net, "CAD (approx)")




#main menu
#not required by the professor, but for making it more smooth,added it

print("Welcome to Programming Prinicples Sample Product Inventory")
print("[1] Add a new item")
print("[2] Display stock statement of a product")
print("[3] Exit the menu")
print()

while True:
    print()
    choice=int(input("enter choice"))
    if choice==1:
        inventory=Inventory()
        Inventory.add(1)
    elif choice==2:
        print("********** Programming Principles Sample Stock Statement*******")
        month=Month()
        Month.display(1)
        Month.months(1)
        
    elif choice==3:
        print("Thanks for using our program")
        break
    else:
        print("please input a valid choice")  


             



        
