# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
#Jack Utzerath
#This is my own Work
def print_hi(name):
    i = True
    j = True
carry = 0
var1 = 0
var2 = 0
print("Half-adder order pairs (sum, carry): ")
# half adder ordered pair output
for x in range(0, 4):
    if x == 0:
        i = True
j = True
if x == 1:
i = True
j = False
if x == 2:
i = False
j = True
if x == 3:
i = False
j = False
# prints carry
carry = (i and j)
# or gate
var1 = (i or j)
# gets the sum
sum = ((not carry) and var1)
# prints out sum and carry in ordered pair
print("(" , int(sum), end="")
print(",", int(carry), ")")
print("\n\nHalf- adder")
# half adder table
for x in range(0, 4):
if x == 0:
i = True
j = True
if x == 1:
i = True
j = False
if x == 2:
i = False
j = True
if x == 3:
i = False
j = False
# carry
carry = (i and j)
# or gate
var1 = (i or j)
# gets the sum
sum = ((not carry) and var1)
# prints out half adder table
print("I = ", int(i), "\tJ = ", int(j), "\t| C=", int(carry), "\tS = ", int(sum), "\t")
#full adder ordered pair output
print("\n\nFull-adder order pairs (sum, carry): ")
# full adder
i = True
j = True
k = True
for x in range(0, 8):
if x == 0:
i = True
j = True
k = True
if x == 1:
i = True
j = True
k = False
if x == 2:
i = True
j = False
k = True
if x == 3:
i = True
j = False
k = False
if x == 4:
i = False
j = True
k = True
if x == 5:
i = False
j = True
k = False
if x == 6:
i = False
j = False
k = True
if x == 7:
i = False
j = False
k = False
carry = (i and j)
# or gate
var1 = (i or j)
# gets the sum
sum = ((not carry) and var1)
var3 = (sum and k)
carry2 = (carry or var3)
var2 = (sum or k)
sum2 = ((not var3) and var2)
print("(", int(sum2), end="")
print(",", int(carry2), ")")
# full adder Table
print("\n\nFull-adder")
# full adder
i = True
j = True
k = True
for x in range(0, 8):
if x == 0:
i = True
j = True
k = True
if x == 1:
i = True
j = True
k = False
if x == 2:
i = True
j = False
k = True
if x == 3:
i = True
j = False
k = False
if x == 4:
i = False
j = True
k = True
if x == 5:
i = False
j = True
k = False
if x == 6:
i = False
j = False
k = True
if x == 7:
i = False
j = False
k = False
carry = (i and j)
# or gate
var1 = (i or j)
# gets the sum
sum = ((not carry) and var1)
var3 = (sum and k)
#gets second carry
carry2 = (carry or var3)
var2 = (sum or k)
# gets second sum
sum2 = ((not var3) and var2)
print("I = ", int(i), "\tJ = ", int(j), "\tK = ", int(k), "\t| C=", int(carry2), "\tS = ", int(sum2), "\t")
# Parallel Adder
print ("\n\nParallel Adder All Solutions\n")
for x in range(0, 8):
if x == 0:
i = True
j = True
k = False
if x == 1:
i = True
j = True
k = False
if x == 2:
i = True
j = False
k = False
if x == 3:
i = True
j = False
k = False
if x == 4:
i = False
j = True
k = False
if x == 5:
i = False
j = True
k = False
if x == 6:
i = False
j = False
k = False
if x == 7:
i = False
j = False
k = False
carry = (i and j)
# or gate
var1 = (i or j)
# gets the sum
sum = ((not carry) and var1)
var3 = (sum and k)
fullAdderCarry = (carry or var3)
var2 = (sum or k)
fullAdderSum = ((not var3) and var2)
for x in range(0, 8):
if x == 0:
l = True
m = True
n = fullAdderCarry
if x == 1:
l = True
m = True
n = fullAdderCarry
if x == 2:
l = True
m = False
n = fullAdderCarry
if x == 3:
l = True
m = False
n = fullAdderCarry
if x == 4:
l = False
m = True
n = fullAdderCarry
if x == 5:
l = False
m = True
n = fullAdderCarry
if x == 6:
l = False
m = False
n = fullAdderCarry
if x == 7:
l = False
m = False
n = fullAdderCarry
carry20 = (l and m)
# or gate
var21 = (l or m)
# gets the sum
sum20 = ((not carry20) and var21)
var23 = (sum20 and n)
fullAdderCarry2 = (carry20 or var23)
var22 = (sum20 or n)
fullAdderSum2 = ((not var23) and var22)
for x in range(0, 8):
if x == 0:
a = True
b = True
c = fullAdderCarry2
if x == 1:
a = True
b = True
c = fullAdderCarry2
if x == 2:
a = True
b = False
c = fullAdderCarry2
if x == 3:
a = True
b = False
c = fullAdderCarry2
if x == 4:
a = False
b = True
c = fullAdderCarry2
if x == 5:
a = False
b = True
c = fullAdderCarry2
if x == 6:
a = False
b = False
c = fullAdderCarry2
if x == 7:
a = False
b = False
c = fullAdderCarry2
carry2 = (a and b)
# or gate
var10 = (a or b)
# gets the sum
sum2 = ((not carry2) and var10)
var12 = (sum2 and c)
fullAdderCarry3 = (carry2 or var12)
var11 = (sum2 or c)
fullAdderSum3 = ((not var12) and var11)
print (int(a), int(l), int(i), end= "")
print(" + ", int(b), int(m), int(j), end = "")
print (" = ", int(fullAdderCarry3), int(fullAdderSum3), int(fullAdderSum2),
int(fullAdderSum))
print("\n")
if __name__ == '__main__':
print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/