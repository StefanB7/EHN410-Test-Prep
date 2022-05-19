#Stefan Buys
#EHN 410 - Toets voorbereiding
#Eucludian Algorithm
#April 2021

import numpy as np

a = 72345
b = 43215

#Swap a and b if a > b
if a > b:
    temp = a
    a = b
    b = temp

print("gcd("+str(a)+","+str(b)+") = ")

bAnswerFound = False
while not(bAnswerFound):
    r = a % b
    if (r <= 0):
        bAnswerFound = True

    a = b
    b = r

    print("\t = gcd("+str(a)+","+str(b)+")")

print("\t = " + str(a))