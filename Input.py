num1=int(input("Enter the number")) #34
num2=int(input("Enter the number")) #32
print(num1+num2)    # o/p = 66


#Reading data on single line 
n,m=input("Enter the number").split(",") #5,7
#it perform concatination 
c=n+m
print(c) #o/p=57


#map()function
a,b=map(int,input("Enter the number").split(","))
print(a+b)