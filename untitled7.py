
 
'''
c=str(input("Enter string to display"))

for i in range(0,10):
   print(c)
   '''
n=int(input("Enter the number:"))
m=int(input("Enter one more number:"))
o=int(input("Enter  third number:"))

if(n>m & n>o):
    print(n," is greater number")
 
elif(m>n & m>o):
    print(m," is greater number")
   
elif(o>m & o>n):
    print(o," is greater number")
    

x=int(input("Enterr a number"))  
    
match x:
    case 0:
        print("number is zero")
    case if(x>=100):
                print("The number is greater then 100")