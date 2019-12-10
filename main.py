'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Operation1 = input("1st number") 
Operation2 = input("2nd number") 
Operation = input("Operation?") 

if (Operation == '+'):
 result = int(Operation1) + int(Operation2)

elif (Operation == '-'):
 result = int(Operation1) - int(Operation2) 

elif (Operation == '*'):
 result = int(Operation1) * int(Operation2) 

elif (Operation == '/'):
 result = int(Operation1) / int(Operation2)

print((result)) 


