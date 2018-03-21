class maths():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b

def Get_int_Value1():
    num = input("Enter first number: ")
    while not num.replace('.', '').replace(',', '').isdigit():
        num = input("You have to type a positive value: ")
    return int(num)
def Get_int_Value2():
    num = input("Enter Second number: ")
    while not num.replace('.', '').replace(',', '').isdigit():
        num = input("You have to type a positive value: ")
    return int(num)

a = Get_int_Value1()
b = Get_int_Value2()
obj=maths(a,b)

def CalC():
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    while True:
        choice=int(input("Enter choice: "))
        try:
            if choice==1:
                print("Result: ",obj.add())
            elif choice==2:
                print("Result: ",obj.sub())
            elif choice==3:
                print("Result: ",obj.mul())
            elif choice==4:
                print("Result: ",round(obj.div(),2))
            elif choice==0:
                print("Exiting!")
                break
            else:
                print("Invalid choice!!")
            continue
        except ValueError:
            print("Do enter correct option")
            pass

CalC()
