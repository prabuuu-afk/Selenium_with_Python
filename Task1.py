#spy number
"""def spynum(n):
n=str(n)
s=0
p=1
for i in n:
    s+=int(i)
    p*=int(i)
if s==p:
    return "spy"
return "not spy"
num=int(input())
print(spynum(num))"""
#digit count
"""def digitcount(n):
count=0
for i in range(len(str(n))):
    count+=1
return count
n=int(input())
print(digitcount(n))"""
#square&cube
"""def square(n):
return n**2
def cube(n):
return n**3
num=int(input())
print(square(num),cube(num))"""
#sum
"""def sum(i,d):
return i+d
i=int(input())
d=float(input())
print(sum(i,d))"""
#capital
"""def isCapital(s):
if s.isupper():
return "Capital"
return "Not a capital"
s=input()
print(isCapital(s))"""
#vowel
"""def isVowel(s):
vov="AEIOUaeiou"
if s in vov:
return "vowel"
return "consonant"
s=input()
print(isVowel(s))"""
#tolowercase
"""def toSmallLetter(s):
    if s.isupper():
        return chr(ord(s)+32)
    return s
s=input()   
print(toSmallLetter(s))"""
#sum of divisors
"""class Divisors:
    def printSumOfDivisors(self, num):
        print("Divisors of", num, "are:", end=" ")
        total = 0
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
                total += i
        print("\nSum of divisors =", total)
n = int(input("Enter a number: "))
obj = Divisors()
obj.printSumOfDivisors(n)"""
#laptop discount
"""class LaptopDiscount:
    def input(self):
        self.price = float(input("Enter the price of the laptop: "))

    def calculateCharge(self):
        if self.price <= 50000:
            discount = 0
        elif self.price <= 100000:
            discount = 0.10 * self.price
        elif self.price <= 150000:
            discount = 0.15 * self.price
        else:
            discount = 0.20 * self.price

        final_price = self.price - discount
        print(f"List Price: ₹{self.price}")
        print(f"Discount: ₹{discount}")
        print(f"Final Price after discount: ₹{final_price}")

lap = LaptopDiscount()
lap.input()
lap.calculateCharge()"""
#splitdigits
"""class SplitDigits:
    def squareDigits(self, num):
        print("Squares of each digit:")
        for digit in str(num):
            sq = int(digit) ** 2
            print(sq, end=", ")
n = int(input("Enter a number: "))
obj = SplitDigits()
obj.squareDigits(n)"""
#one and two digit sum
"""class NumberArray:
    def __init__(self):
        self.arr = []

    def acceptValues(self):
        print("Enter 10 integers:")
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            self.arr.append(num)

    def calculateSums(self):
        one_digit_sum = 0
        two_digit_sum = 0

        for num in self.arr:
            if 0 <= num <= 9:
                one_digit_sum += num
            elif 10 <= num <= 99:
                two_digit_sum += num

        print("Sum of one-digit numbers:", one_digit_sum)
        print("Sum of two-digit numbers:", two_digit_sum)
obj = NumberArray()
obj.acceptValues()
obj.calculateSums()"""
#Sequence functions
'''def series1():
    for i in range(2, 18, 2):
        print(i, end=" ")
    print()

def series2():
    for i in range(50, -10, -10):
        print(i, end=" ")
    print()
series1()
series2()'''

#Square and cube functions
'''def square(a):
    print("Square:", a ** 2)

def cube(b):
    print("Cube:", b ** 3)
square(5)
cube(3)'''

#Split digits
'''def splitDigits(num):
    print("Digits separated:")
    while num > 0:
        digit = num % 10
        print(digit, end=" ")
        num //= 10
    print()
splitDigits(4327)'''

#Armstrong number check
'''def printArmstrong(n):
    temp = n
    digits = len(str(n))
    sum_val = 0
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** digits
        temp //= 10
    if sum_val == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")
printArmstrong(153)'''

#Spy number check
'''def isSpyNumber(n):
    sum_digits = 0
    product_digits = 1
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        product_digits *= digit
        temp //= 10
    if sum_digits == product_digits:
        print(n, "is a Spy number")
    else:
        print(n, "is not a Spy number")
isSpyNumber(1124)'''

#Square of each digit
'''def squareDigits(num):
    print("Squares of digits:")
    while num > 0:
        digit = num % 10
        print(digit ** 2, end=" ")
        num //= 10
    print()
squareDigits(42316)'''

#Count digits
'''def countDigits(num):
    count = len(str(num))
    print("Number of digits:", count)
countDigits(34562)'''