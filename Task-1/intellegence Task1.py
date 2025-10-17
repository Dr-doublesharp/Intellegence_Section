
# 1 - Variable Swapper
print("\n1 - Variable Swapper")
var1 = 5
var2 = 100
print ("\nOld Variables Are\nvar1: " +str(var1) + " var2: " + str(var2))
temp = var1
var1 = var2
var2 = temp
print ("\nNew Variables Are\nvar1: " +str(var1) +" var2: " + str(var2))
print("\n--------------------------------------------------------------------------------")



# 2 - Find Largest Number
print("\n2 - Find Largest Number")
a = 30
b= 20
c = 50
if a>b:
    if a>c:
        print (" a is Bigger: " + str(a))
    else:
        print (" c is Bigger: " + str(c))
elif b>c:
    print (" b is Bigger: " + str(b))
else:
    print (" c is Bigger: " + str(c))
print("\n--------------------------------------------------------------------------------")



#3 - print pattern 1 2 3 4 5
print("\n3 - print pattern 1 2 3 4 5")

list = [1,2,3,4,5]
i = len(list)
while i>0:
    print(list[:i])
    i = i-1
print("\n--------------------------------------------------------------------------------")



#4 - print odd numbers from 1 to n
print("\n4 - print odd numbers from 1 to n")
print("\n Enter Last Number: ")
n = int(input())

while n >= 0:
    if n%2 != 0:
        print(n)
    n = n-1
print("\n--------------------------------------------------------------------------------")



#5 - check if string is palindrome (اذا عكست النص فانه سيكون نفسه مثل توت)
print("\n5 - check if string is palindrome")
print("\n enter a pallindrome text: ")
s = input()
if s == s[len(s) : : -1]:
    print ("this text is Pallindrome")
else:
    print("this text isn't Palindrome")
print("\n--------------------------------------------------------------------------------")



#6 - return first 2 & last 2 char from string
print("\n6 - return first 2 & last 2 char from string")
print("\nEnter Text: ")
s = input()

if len(s) < 3:
    print("")
else:
    print(s[0:2] + s[len(s) -2 : len(s)])
print("\n--------------------------------------------------------------------------------")



#7 - remove (n) index from text
print("\n7 - remove (n) index from text")
print("\nHello World")
text = "Hello World"
print("Enter Index to remove")
i = int(input())
if i>len(text) | i<0:
    print("wrong index")
else:
    if i == len(text):
        print(text[:])
    elif i == 0:
        print(text[1:])
    else:
        print(text[:i] + text[i+1:])
print("\n--------------------------------------------------------------------------------")



#8 - check prime number function
print("\n8 - check prime number function")

def isPrime (num):
    if num == 0 | num == 1:
        print("Wrong Number")
        return
    i = 2
    checkPrime = True
    while i<num:
        if num%i ==0:
            checkPrime = False
            break
        i = i+1
    if checkPrime == True:
        print("The Number " + str(num) +" Is A Prime Number")
    else:
        print("The Number " + str(num) +" Is Not A Prime Number")

print("Enter A Number To Check Whether It's Prime Or Not:")
i = int(input())
isPrime(i)
print("\n--------------------------------------------------------------------------------")



print("\n Press Enter To End Program")
i = input()