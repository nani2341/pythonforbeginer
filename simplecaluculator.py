print('''please enter the option you want to perform
      1.add
      2.subtract
      3.multiplication
      4.division''')
option=int(input("please enter the option"))
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if option==1:
    print("num1","+","num2","=",num1+num2)
elif option==2:
    print("num1","-","num2","=",num1-num2)
elif option==3:
    print("num1","*","num2","=",num1*num2)
elif option==4:
    print("num1","/","num2","=",num1/num2)
else:
    print("invalid input")
           
