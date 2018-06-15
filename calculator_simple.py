class calculator:
    print("Welcome to a simple calculator")
    global x
    x=int(input("1st number : "))
    global y
    y=int(input("2nd number : "))
    def add(self,i,j):
        self.i=i
        self.j=j
        return self.i+self.j
    def sub(self,i,j):
        self.i=i
        self.j=j
        if(i>j):
            return self.i-self.j
        else:
            return self.j-self.i
    def pro(self,i,j):
        self.i=i
        self.j=j
        return self.i*self.j
    def div(self,i,j):
        self.i=i
        self.j=j
        return self.i/self.j
        

cal=calculator()
n=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division of the two numbers : "))
if n==1:
    print("Sum = " , cal.add(x,y))
elif n==2:
    print("Difference = " , cal.sub(x,y))
elif n==3:
    print("Product = " , cal.pro(x,y))
elif n==4:
    print("Division = " , cal.div(x,y))
else:
    print("Enter Correct option")
input("Press ENTER to exit")
